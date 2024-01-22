import sys
sys.path.append('presets') 

import pygame
import random
import numpy as np
import pandas as pd
from Presets import _PRESETS
from colors.MakeColors import filter_leaf_colors
from LeafPresets import *

def _roulette_selection(rules):
    rand = random.random()
    sum_odds = 0
    for rule in rules:
        sum_odds += rule['odds']
        if rand < sum_odds:
            return rule
    return rules[-1]

class Botanica:
    def __init__(self, preset_index=None):
        if preset_index is None:
            preset_index = random.randint(0, len(_PRESETS) - 1)
        else:
            preset_index = max(0, min(preset_index, len(_PRESETS) - 1))

        self.colors = pd.read_csv('presets\colors\colors_preset.csv')['Color'].tolist()
        self.leaf_colors = filter_leaf_colors(self.colors)

        self._axiom = _PRESETS[preset_index]['axiom']
        self._rules = _PRESETS[preset_index]['rules']

        self.iterations = 4
        self._sentence = []
        self._angles = []
        self._leaf_angles = []

    def _apply_rules_to_sentence(self, sentence):
        new_sentence = []
        for c in sentence:
            matching_rules = [rule for rule in self._rules if rule['symbol'] == c]
            if matching_rules:
                rule = _roulette_selection(matching_rules)
                new_sentence.extend(rule['newSymbols'])
            else:
                new_sentence.append(c)
        return new_sentence

    def _apply_rules(self):
        cur = self._axiom
        for _ in range(self.iterations):
            cur = self._apply_rules_to_sentence(cur)
        self._sentence = cur

    
    def _calculate_scale_factor(self):
        current_pos = np.array([0, 0])
        max_pos = np.array([0, 0])
        min_pos = np.array([0, 0])
        max_x = 0
        max_y = 0
        min_x = 0
        min_y = 0
        angle = 90
        stack = []

        for c in self._sentence:
            if c == 'F' or c == 'X':
                next_pos = current_pos + np.array([np.cos(np.radians(angle)), -np.sin(np.radians(angle))])
                current_pos = next_pos
                max_x = np.maximum(max_x, current_pos[0])
                min_x = np.minimum(min_x, current_pos[0])

                max_y = np.maximum(max_y, current_pos[1])
                min_y = np.minimum(min_y, current_pos[1])

            elif c in '+-':
                angle_change = random.uniform(18, 30)
                angle += angle_change if c == '+' else -angle_change
            elif c == '[':
                stack.append((current_pos.copy(), angle))
            elif c == ']':
                current_pos, angle = stack.pop()

        plant_width = max_x - min_x
        plant_height = max_y - min_y

        screen_width, screen_height = pygame.display.get_surface().get_size()
        
         # Prilagodjavanje scale_factor u odnosu na sirinu i visinu
        width_ratio = screen_width / plant_width if plant_width != 0 else float('inf')
        height_ratio = screen_height / plant_height if plant_height != 0 else float('inf')
        scale_factor = min(width_ratio, height_ratio) * 0.8

        if plant_height * scale_factor > screen_height * 0.9 or plant_width * scale_factor > screen_width * 0.9:
            scale_factor = min((screen_height * 0.9) / plant_height, (screen_width * 0.9) / plant_width) * 0.8

        # Ogranicavanje visine da ne prelazi 90% visine ekrana
        if plant_height * scale_factor > screen_height * 0.9:
            scale_factor = (screen_height * 0.9) / plant_height

        return scale_factor

    def _generate_plant(self):
        self._angles = []
        self._leaf_angles = []
        self._leaf_size = []
        self.leaf_shape = random.choice(leaf_shapes)

        self.color = pygame.Color(random.choice(self.colors))
        self.leaf_color = pygame.Color(random.choice(self.leaf_colors))
        self.color_2 = pygame.Color(random.choice(self.colors))

        for c in self._sentence:
            if c == '+':
                self._angles.append(random.uniform(18, 28))
            elif c == '-':
                self._angles.append(-random.uniform(18, 28))
            elif c in 'G]':
                self._leaf_angles.append(np.random.uniform(0, 360))
                self._leaf_size.append(np.random.uniform(0.21, 0.27))
        
    def _render_leaf(self, leaf_color, current_pos, time, cnt):
        if 0 <= current_pos[0] < screen.get_width() and 0 <= current_pos[1] < screen.get_height():
            leaf_scale_factor = self._leaf_size[cnt]
            leaf_width_factor = leaf_scale_factor * screen.get_width() / 100
            leaf_height_factor = leaf_scale_factor * screen.get_height() / 100

            # Nasumican ugao rotacije za list
            rotation_angle = self._leaf_angles[cnt]
            sway_angle = 0.28 * np.sin(time * 0.04) 
            rotation_angle += sway_angle
            self._leaf_angles[cnt] = rotation_angle

            rotation_matrix = np.array([
                [np.cos(np.radians(rotation_angle)), -np.sin(np.radians(rotation_angle))],
                [np.sin(np.radians(rotation_angle)), np.cos(np.radians(rotation_angle))]
            ])

            # Rotiranje i skaliranje oblika lisca
            rotated_scaled_leaf_shape = []
            for x, y in self.leaf_shape:
                rotated_point = np.dot(rotation_matrix, np.array([x, y]))
                scaled_x = rotated_point[0] * leaf_width_factor + current_pos[0]
                scaled_y = rotated_point[1] * leaf_height_factor + current_pos[1]
                rotated_scaled_leaf_shape.append((scaled_x, scaled_y))

            pygame.draw.polygon(screen, leaf_color, rotated_scaled_leaf_shape)

        
    def _render(self, screen, scale_factor, time):
        screen.fill(pygame.Color('#000000'))
        current_pos = np.array([screen.get_width() / 2, screen.get_height() - 50])

        angle = 90
        growth_factor = 7  # Pocetna debljina grane

        stack = []
        growth_factor_stack = []  # Stek za pamcenje prethodnih vrednosti growth_factor
        angle_cnt = 0
        leaf_cnt = 0

        for c in self._sentence:
            if c == 'F':
                next_pos = current_pos + (np.array([np.cos(np.radians(angle)), -np.sin(np.radians(angle))]) * scale_factor)
                pygame.draw.line(screen, self.color, current_pos.astype(int), next_pos.astype(int), int(growth_factor))
                current_pos = next_pos
            
            elif c == 'X':
                next_pos = current_pos + (np.array([np.cos(np.radians(angle)), -np.sin(np.radians(angle))]) * scale_factor)
                pygame.draw.line(screen, self.color, current_pos.astype(int), next_pos.astype(int), int(growth_factor))
                current_pos = next_pos

            elif c == 'G':
                self._render_leaf(self.leaf_color, current_pos, time, leaf_cnt)
                leaf_cnt += 1

            elif c == 'Z':
                if 0 <= current_pos[0] < screen.get_width() and 0 <= current_pos[1] < screen.get_height():
                    pygame.draw.circle(screen, (255, 0, 0), current_pos.astype(int), 8, 0)

            elif c in '+-':
                angle += self._angles[angle_cnt]
                angle_cnt += 1

            elif c == '[':
                stack.append((current_pos.copy(), angle))
                growth_factor_stack.append(growth_factor)
                growth_factor *= 0.85  # Smanji growth_factor za nove grane

            elif c == ']':
                self._render_leaf(self.leaf_color, current_pos, time, leaf_cnt)
                current_pos, angle = stack.pop()
                growth_factor = growth_factor_stack.pop()  # Vrati growth_factor na prethodnu vrednost
                leaf_cnt += 1

        pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((750, 600)) 
pygame.display.set_caption('Botanica Algorithmica')

app = Botanica()
app._apply_rules()
scale_factor = app._calculate_scale_factor()
#app._render(screen, scale_factor, offset, time)
app._generate_plant()

running = True
need_redraw = True
time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    if need_redraw:
        app._render(screen, scale_factor, time)
        need_redraw = True
    time += 1  # Ažuriranje vremena

    pygame.display.flip()

pygame.quit()