import sys
sys.path.append('presets') 

from Presets import _PRESETS

import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def _roulette_selection(rules):
    rand = random.random()
    sum_odds = 0
    for rule in rules:
        sum_odds += rule['odds']
        if rand < sum_odds:
            return rule
    return rules[-1]

class LSystemDemo:
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

    def _render(self):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')

        stack = []
        current_pos = np.array([0, 0])
        angle = 90 

        color = random.choice(self.colors)

        for c in self._sentence:
            if c == 'F':
                next_pos = current_pos + np.array([np.cos(np.radians(angle)), np.sin(np.radians(angle))])
                ax.plot([current_pos[0], next_pos[0]], [current_pos[1], next_pos[1]], color=color, linestyle='-')
                current_pos = next_pos
            elif c == 'G':
                ax.plot(current_pos[0], current_pos[1], 'go', markersize=3) 
            elif c == 'Z':
                ax.plot(current_pos[0], current_pos[1], 'mo', markersize=4) 
            elif c == '+':
                angle_change = random.uniform(12, 35)
                angle += angle_change
            elif c == '-':
                angle_change = random.uniform(12, 35)
                angle -= angle_change
            elif c == '[':
                stack.append((current_pos, angle))
            elif c == ']':
                current_pos, angle = stack.pop()

        ax.axis('off')
        plt.show()

app = LSystemDemo(iterations=3)
app._apply_rules()
app._render()
