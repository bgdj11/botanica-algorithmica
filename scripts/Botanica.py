import sys
sys.path.append('presets') 

import pygame
import random
import math
import time
import numpy as np
import pandas as pd
from Presets import _PRESETS
from colors.MakeColors import filter_leaf_colors, filter_non_green_colors
from LeafPresets import *
from FruitPresets import *

PLANT_SCREEN_WIDTH = 808
PLANT_SCREEN_HEIGHT = 650

SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1362

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

        self.colors = pd.read_csv('presets\colors\colors_preset.csv')['Color'].tolist()
        self.fruit_colors = pd.read_csv('presets\\colors\\fruit_colors_preset.csv')['Color'].tolist()
        self.leaf_colors = filter_leaf_colors(self.colors)
        self.flower_colors = pd.read_csv('presets\\colors\\flower_colors_preset.csv')['Color'].tolist()

        self.max_iterations = 4 
        self.iterations = self.max_iterations 
        self.growth_factor = 7
        self.max_growth_factor = 15  
        self.min_growth_factor = 3   

        # Inicijalizacija za slajdere
        self.dragging_slider = False 
        self.dragging_growth_factor_slider = False 

        # Definisanje pravougaonika za slajdere i dugmad
        button_width = 350
        button_height = 80
        slider_width = 350
        slider_height = 20
        handle_width = 15
        handle_height = 20
        spacing = 30
        text_offset = 20
        margin = 10

        generate_button_width = int(button_width * 0.75) 
        save_button_width = button_width - generate_button_width  
        
        self.generate_button_rect = pygame.Rect(100, 80, generate_button_width - margin // 2, 80)
        self.save_button_rect = pygame.Rect(100 + generate_button_width + margin // 2, 80, save_button_width - margin // 2, 80)


        self.iterations_slider_rect = pygame.Rect(100, 200 + text_offset, slider_width, slider_height)
        self.iterations_handle_rect = pygame.Rect(100 + slider_width * (self.iterations - 1) / (self.max_iterations - 1), 200 + text_offset, handle_width, handle_height)

        self.growth_factor_slider_rect = pygame.Rect(100, 260 + text_offset, slider_width, slider_height)
        self.growth_factor_handle_rect = pygame.Rect(
            100 + (self.growth_factor - self.min_growth_factor) * \
            slider_width / (self.max_growth_factor - self.min_growth_factor),
            260 + text_offset, 
            handle_width, 
            handle_height
        )

        self.random_leaf_button_rect = pygame.Rect(100, 290 + text_offset + spacing, button_width, button_height)

        self.change_stem_color_button_rect = pygame.Rect(100, 380 + text_offset + 2 * spacing, button_width // 2 - 5, button_height)
        self.change_leaf_color_button_rect = pygame.Rect(100 + button_width // 2 + 5, 380 + text_offset + 2 * spacing, button_width // 2 - 5, button_height)


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

        screen_width = PLANT_SCREEN_WIDTH
        screen_height = PLANT_SCREEN_HEIGHT
        
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

        self.preset_index = random.randint(0, len(_PRESETS) - 1)

        self._axiom = _PRESETS[self.preset_index]['axiom']
        self._rules = _PRESETS[self.preset_index]['rules']

        self.growth_factor = 7
        self.iterations = 4
        self._sentence = []
        self._angles = []
        self._leaf_angles = []
        self._leaf_size = []
        self._fruit_size = []
        self._flower_size = []
        self._fruit_angles = []

        self.flower_or_fruit = random.randint(0,1)

        self.leaf_shape = random.choice(leaf_shapes)
        self.fruit_shape = random.choice(fruit_shapes)

        self.color = pygame.Color(random.choice(self.colors))
        self.leaf_color = pygame.Color(random.choice(self.leaf_colors))
        self.fruit_color = pygame.Color(random.choice(self.fruit_colors))
        self.petal_color = pygame.Color(random.choice(self.flower_colors))

        self._apply_rules()

        for c in self._sentence:
            if c == '+':
                self._angles.append(random.uniform(18, 28))
            elif c == '-':
                self._angles.append(-random.uniform(18, 28))
            elif c in 'G]':
                self._leaf_angles.append(np.random.uniform(0, 360))
                self._leaf_size.append(np.random.uniform(0.21, 0.27))
            elif c == 'Z':
                self._fruit_size.append(np.random.uniform(0.21, 0.27))
                self._flower_size.append(np.random.uniform(0.4, 0.6))
                self._fruit_angles.append(np.random.uniform(0, 360))

        # Vracanje slajdera na pocetnu poziciju
        self.iterations_handle_rect.x = (
            self.iterations_slider_rect.x +
            (self.iterations_slider_rect.width - self.iterations_handle_rect.width) *
            (self.iterations - 1) / (self.max_iterations - 1)
        )

        self.growth_factor_handle_rect.x = (
            self.growth_factor_slider_rect.x +
            (self.growth_factor - self.min_growth_factor) *
            (self.growth_factor_slider_rect.width - 10) /
            (self.max_growth_factor - self.min_growth_factor)
        )

        return self._calculate_scale_factor()

    def _modify_plant(self):
        self._sentence = []
        self._apply_rules()

        self._angles = []
        self._leaf_angles = []
        self._leaf_size = []
        self._fruit_size = []
        self._flower_size = []
        self._fruit_angles = []

        for c in self._sentence:
            if c == '+':
                self._angles.append(random.uniform(18, 28))
            elif c == '-':
                self._angles.append(-random.uniform(18, 28))
            elif c in 'G]':
                self._leaf_angles.append(np.random.uniform(0, 360))
                self._leaf_size.append(np.random.uniform(0.21, 0.27))
            elif c == 'Z':
                self._fruit_size.append(np.random.uniform(0.21, 0.27))
                self._flower_size.append(np.random.uniform(0.4, 0.6))
                self._fruit_angles.append(np.random.uniform(0, 360))
        
    def _render_fruit(self, screen, current_pos, cnt):
        if 0 <= current_pos[0] < screen.get_width() and 0 <= current_pos[1] < screen.get_height():
            fruit_scale_factor = self._fruit_size[cnt]
            fruit_width_factor = fruit_scale_factor * PLANT_SCREEN_WIDTH/100
            fruit_height_factor = fruit_scale_factor * PLANT_SCREEN_HEIGHT/100

            rotation_angle = self._fruit_angles[cnt]

            rotation_matrix = np.array([
                [np.cos(np.radians(rotation_angle)), -np.sin(np.radians(rotation_angle))],
                [np.sin(np.radians(rotation_angle)), np.cos(np.radians(rotation_angle))]
            ])

            # Rotiranje i skaliranje
            rotated_scaled_fruit_shape = []
            for x, y in self.fruit_shape:
                rotated_point = np.dot(rotation_matrix, np.array([x, y]))
                scaled_x = rotated_point[0] * fruit_width_factor + current_pos[0]
                scaled_y = rotated_point[1] * fruit_height_factor + current_pos[1]
                rotated_scaled_fruit_shape.append((scaled_x, scaled_y))

            pygame.draw.polygon(screen, self.fruit_color, rotated_scaled_fruit_shape)

    def _render_flower(self, screen, current_pos, cnt):
        if 0 <= current_pos[0] < screen.get_width() and 0 <= current_pos[1] < screen.get_height():
            base_petal_radius = 11
            base_center_radius = 8
            num_petals = 5

            center_color = (246, 218, 31)
            
            flower_scale_factor = self._flower_size[cnt]

            petal_radius = base_petal_radius * flower_scale_factor
            center_radius = base_center_radius * flower_scale_factor
            
            for i in range(num_petals):
                angle = (360 / num_petals) * i
                radian = np.radians(angle)
                petal_x = current_pos[0] + np.cos(radian) * petal_radius
                petal_y = current_pos[1] + np.sin(radian) * petal_radius
                pygame.draw.circle(screen, self.petal_color, (int(petal_x), int(petal_y)), int(petal_radius))
            
            pygame.draw.circle(screen, center_color, current_pos.astype(int), int(center_radius))
        
    def _render_leaf(self, screen, leaf_color, current_pos, time, cnt):
        if 0 <= current_pos[0] < screen.get_width() and 0 <= current_pos[1] < screen.get_height():
            leaf_scale_factor = self._leaf_size[cnt]
            leaf_width_factor = leaf_scale_factor * PLANT_SCREEN_WIDTH / 100
            leaf_height_factor = leaf_scale_factor * PLANT_SCREEN_HEIGHT / 100

            # Nasumican ugao rotacije za list
            rotation_angle = self._leaf_angles[cnt]
            sway_angle = 0.25 * np.sin(time * 0.04) 
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
        current_pos = np.array([2 * SCREEN_WIDTH / 3 + 25, PLANT_SCREEN_HEIGHT])

        angle = 90
        stack = []
        growth_factor_stack = [] 
        angle_cnt = 0
        leaf_cnt = 0
        fruit_cnt = 0

        flower_positions = []
        flower_counter = []

        for c in self._sentence:
            if c == 'F':
                next_pos = current_pos + (np.array([np.cos(np.radians(angle)), -np.sin(np.radians(angle))]) * scale_factor)
                pygame.draw.line(screen, self.color, current_pos.astype(int), next_pos.astype(int), int(self.growth_factor))
                current_pos = next_pos
            
            elif c == 'X':
                next_pos = current_pos + (np.array([np.cos(np.radians(angle)), -np.sin(np.radians(angle))]) * scale_factor)
                pygame.draw.line(screen, self.color, current_pos.astype(int), next_pos.astype(int), int(self.growth_factor))
                current_pos = next_pos

            elif c == 'G':
                self._render_leaf(screen, self.leaf_color, current_pos, time, leaf_cnt)
                leaf_cnt += 1

            elif c == 'Z':
                if(self.flower_or_fruit == 0):
                    flower_positions.append(current_pos)
                    flower_counter.append(fruit_cnt)
                else:
                    self._render_fruit(screen, current_pos, fruit_cnt)
                fruit_cnt += 1

            elif c in '+-':
                angle += self._angles[angle_cnt]
                angle_cnt += 1

            elif c == '[':
                stack.append((current_pos.copy(), angle))
                growth_factor_stack.append(self.growth_factor)
                self.growth_factor *= 0.85  # Smanji growth_factor za nove grane

            elif c == ']':
                self._render_leaf(screen, self.leaf_color, current_pos, time, leaf_cnt)
                current_pos, angle = stack.pop()
                self.growth_factor = growth_factor_stack.pop()  # Vrati growth_factor na prethodnu vrednost
                leaf_cnt += 1
        
        # Renderovanje cvetova na kraju
        for i, position in enumerate(flower_positions):
            self._render_flower(screen, position, flower_counter[i])


        pygame.display.flip()

    def _render_ui(self, screen):

        button_color = (71, 58, 43)
        text_color = (84, 117, 91)
        font = pygame.font.Font(None, 32)

        # Labele
        iterations_label_text = font.render('See development', True, text_color)
        screen.blit(iterations_label_text, (100, 200))

        growth_factor_label_text = font.render('Branches width', True, text_color)
        screen.blit(growth_factor_label_text, (100, 260))
        
        # Dugme "Generate Again"
        pygame.draw.rect(screen, button_color, self.generate_button_rect)
        generate_button_text = font.render('GENERATE NEW', True, text_color)
        generate_text_rect = generate_button_text.get_rect(center=self.generate_button_rect.center)
        screen.blit(generate_button_text, generate_text_rect)

        # Dugme "Save"
        pygame.draw.rect(screen, button_color, self.save_button_rect)
        save_button_text = font.render('SAVE', True, text_color)
        save_text_rect = save_button_text.get_rect(center=self.save_button_rect.center)
        screen.blit(save_button_text, save_text_rect)
        
        # Slajder za Iteracije
        pygame.draw.rect(screen, (180, 180, 180), self.iterations_slider_rect)  
        pygame.draw.rect(screen, (100, 100, 100), self.iterations_handle_rect)  

        # Slajder sa Growth Factor
        pygame.draw.rect(screen, (180, 180, 180), self.growth_factor_slider_rect) 
        pygame.draw.rect(screen, (100, 100, 100), self.growth_factor_handle_rect) 

        # Dugme "New leaves"
        pygame.draw.rect(screen, button_color, self.random_leaf_button_rect)
        random_leaf_button_text = font.render('CHANGE LEAVES', True, text_color)
        text_rect = random_leaf_button_text.get_rect(center=self.random_leaf_button_rect.center)
        screen.blit(random_leaf_button_text, text_rect)

        small_font = pygame.font.Font(None, 24)

        # Dugme "Change stem color"
        pygame.draw.rect(screen, button_color, self.change_stem_color_button_rect)
        change_stem_color_text_lines = ['CHANGE', 'STEM COLOR']
        stem_text_rect = self.change_stem_color_button_rect.copy()
        total_text_height = small_font.get_linesize() * len(change_stem_color_text_lines)
        stem_text_rect.y -= total_text_height // 4  

        for line in change_stem_color_text_lines:
            rendered_text = small_font.render(line, True, text_color)
            text_rect = rendered_text.get_rect(center=stem_text_rect.center)
            screen.blit(rendered_text, text_rect)
            stem_text_rect.y += small_font.get_linesize()  

        # Dugme "Change leaf color"
        pygame.draw.rect(screen, button_color, self.change_leaf_color_button_rect)
        change_leaf_color_text_lines = ['CHANGE', 'LEAF COLOR']
        leaf_text_rect = self.change_leaf_color_button_rect.copy()
        total_text_height = small_font.get_linesize() * len(change_leaf_color_text_lines)
        leaf_text_rect.y -= total_text_height // 4 

        for line in change_leaf_color_text_lines:
            rendered_text = small_font.render(line, True, text_color)
            text_rect = rendered_text.get_rect(center=leaf_text_rect.center)
            screen.blit(rendered_text, text_rect)
            leaf_text_rect.y += small_font.get_linesize()  


    def _handle_slider_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.iterations_handle_rect.collidepoint(event.pos):
                self.dragging_slider = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging_slider = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging_slider:
                self.iterations_handle_rect.x = max(
                    min(event.pos[0], self.iterations_slider_rect.right - self.iterations_handle_rect.width),
                    self.iterations_slider_rect.x
                )
                self.iterations = 1 + round(
                    (self.iterations_handle_rect.x - self.iterations_slider_rect.x) *
                    (self.max_iterations - 1) / (self.iterations_slider_rect.width - self.iterations_handle_rect.width)
                )
                return True
        return False

    def _handle_growth_factor_slider_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.growth_factor_handle_rect.collidepoint(event.pos):
                self.dragging_growth_factor_slider = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging_growth_factor_slider = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging_growth_factor_slider:
                self.growth_factor_handle_rect.x = max(
                    min(event.pos[0], self.growth_factor_slider_rect.right - 10),
                    self.growth_factor_slider_rect.x
                )
                self.growth_factor = self.min_growth_factor + int(
                    (self.growth_factor_handle_rect.x - self.growth_factor_slider_rect.x) *
                    (self.max_growth_factor - self.min_growth_factor) / 
                    (self.growth_factor_slider_rect.width - 10)
                )
                return True
        return False
