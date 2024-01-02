import random
import matplotlib.pyplot as plt
import numpy as np

# Funkcija za odabir pravila
def _roulette_selection(rules):
    rand = random.random()
    sum_odds = 0
    for rule in rules:
        sum_odds += rule['odds']
        if rand < sum_odds:
            return rule
    return rules[-1]

# Kompletna lista preseta
_PRESETS = [
    {
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.33, 'newSymbols': 'F[+F]F[-F][F]'},
            {'symbol': 'F', 'odds': 0.33, 'newSymbols': 'F[+F][F]'},
            {'symbol': 'F', 'odds': 0.34, 'newSymbols': 'F[-F][F]'},
        ]
    },
    {
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'F+[-F-GF-G][+FF][--GF[+G]][++F-G]'},
        ]
    },
    {
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF+[+F-F-F]-[-F+F+F]'},
        ]
    },
    {
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FG[FG[+GF]]'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'FF[+GZ++G-F[+GZ]][-G++F-G]'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[+F-G-F][++GZ]'},
        ]
    },
    {
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'F[+F]F[-F]F'},
        ]
    },
    {
        'axiom': 'G',
        'rules': [
            {'symbol': 'G', 'odds': 0.33, 'newSymbols': 'F[+G]F[-G]+G'},
            {'symbol': 'G', 'odds': 0.33, 'newSymbols': 'F[-G]F[-G]+G'},
            {'symbol': 'G', 'odds': 0.34, 'newSymbols': 'F[-G]F+G'},
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
        ]
    },
    {
        'axiom': 'G',
        'rules': [
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'F[-[[G]+G]]+F[+FG]-G'},
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
        ]
    }
]


class LSystemDemo:
    def __init__(self, preset_index=0, iterations=5):
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
        angle = 90  # Početni ugao postavljen na 90 stepeni

        for c in self._sentence:
            if c == 'F':
                next_pos = current_pos + np.array([np.cos(np.radians(angle)), np.sin(np.radians(angle))])
                ax.plot([current_pos[0], next_pos[0]], [current_pos[1], next_pos[1]], 'g-')
                current_pos = next_pos
            elif c == 'G':
                # Dodavanje manje zelene tačke za 'G'
                ax.plot(current_pos[0], current_pos[1], 'go', markersize=3)  # Zelena tačka manje veličine
            elif c == 'Z':
                # Dodavanje roze tačke za 'Z'
                ax.plot(current_pos[0], current_pos[1], 'mo', markersize=4)  # Roza tačka
            elif c == '+':
                angle += 25  # Rotira za 25 stepeni u smeru kazaljke na satu
            elif c == '-':
                angle -= 25  # Rotira za 25 stepeni suprotno od smera kazaljke na satu
            elif c == '[':
                stack.append((current_pos, angle))
            elif c == ']':
                current_pos, angle = stack.pop()

        ax.axis('off')
        plt.show()



app = LSystemDemo(preset_index=3, iterations=3)
app._apply_rules()
app._render()
