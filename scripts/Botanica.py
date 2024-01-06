import sys
sys.path.append('presets') 

import pygame
import random
import numpy as np
import pandas as pd
from Presets import _PRESETS

def _roulette_selection(rules):
    rand = random.random()
    sum_odds = 0
    for rule in rules:
        sum_odds += rule['odds']
        if rand < sum_odds:
            return rule
    return rules[-1]

class Botanica:
    def __init__(self, preset_index=None, iterations=5):
        if preset_index is None:
            preset_index = random.randint(0, len(_PRESETS) - 1)
        else:
            preset_index = max(0, min(preset_index, len(_PRESETS) - 1))

        self.colors = pd.read_csv('presets\colors\colors_preset.csv')['Color'].tolist()

        self._axiom = _PRESETS[preset_index]['axiom']
        self._rules = _PRESETS[preset_index]['rules']
        self.iterations = iterations
        self._sentence = []

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
            if c == 'F':
                next_pos = current_pos + np.array([np.cos(np.radians(angle)), -np.sin(np.radians(angle))])
                current_pos = next_pos
                max_x = np.maximum(max_x, current_pos[0])
                min_x = np.minimum(min_x, current_pos[0])

                max_y = np.maximum(max_y, current_pos[1])
                min_y = np.minimum(min_y, current_pos[1])

            elif c in '+-':
                angle_change = random.uniform(15, 35)
                angle += angle_change if c == '+' else -angle_change
            elif c == '[':
                stack.append((current_pos.copy(), angle))
            elif c == ']':
                current_pos, angle = stack.pop()


        plant_width = max_x - min_x
        plant_height = max_y - min_y

        screen_width, screen_height = pygame.display.get_surface().get_size()
        
        # Skaliranje u odnosu na sirinu i visinu
        scale_factor = min(screen_width / plant_width, screen_height / plant_height) * 0.75

        # Pomeranje horizontalno ako je biljka presiroka
        horizontal_offset = 0
        if plant_width * scale_factor > screen_width * 2 / 3 :
            horizontal_offset = (screen_width - plant_width * scale_factor) / 2

        # Pomeranje vertikalno
        vertical_offset = 0
        if plant_height * scale_factor > screen_height:
            vertical_offset = (screen_height - plant_height * scale_factor) / 2

        return scale_factor, np.array([horizontal_offset, vertical_offset])

    def _render(self, screen, scale_factor, offset):
        screen.fill(pygame.Color('#b2d6d0'))

        # Pocetna pozicija bez offseta
        current_pos = np.array([screen.get_width() / 2, screen.get_height() - 50]) + offset

        angle = 90
        stack = []

        color = pygame.Color(random.choice(self.colors))
        color_1 = pygame.Color(random.choice(self.colors))
        color_2 = pygame.Color(random.choice(self.colors))

        for c in self._sentence:
            if c == 'F':
                next_pos = current_pos + (np.array([np.cos(np.radians(angle)), -np.sin(np.radians(angle))]) * scale_factor)
                pygame.draw.line(screen, color, current_pos.astype(int), next_pos.astype(int), 4)
                current_pos = next_pos
            elif c == 'G':
                if 0 <= current_pos[0] < screen.get_width() and 0 <= current_pos[1] < screen.get_height():
                    pygame.draw.circle(screen, color_1, current_pos.astype(int), 5, 0)
            elif c == 'Z':
                if 0 <= current_pos[0] < screen.get_width() and 0 <= current_pos[1] < screen.get_height():
                    pygame.draw.circle(screen, color_2, current_pos.astype(int), 4, 0)
            elif c == '+':
                angle += random.uniform(15, 35)
                angle %= 360
            elif c == '-':
                angle -= random.uniform(15, 35)
                angle %= 360
            elif c == '[':
                stack.append((current_pos.copy(), angle))
            elif c == ']':
                current_pos, angle = stack.pop()

        pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((900, 800)) 
pygame.display.set_caption('Botanica Algorithmica')

app = Botanica(iterations=4)
app._apply_rules()
scale_factor, offset = app._calculate_scale_factor()
app._render(screen, scale_factor, offset)

running = True
need_redraw = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    if need_redraw:
        app._render(screen, scale_factor, offset)
        need_redraw = False

    pygame.display.flip()

pygame.quit()