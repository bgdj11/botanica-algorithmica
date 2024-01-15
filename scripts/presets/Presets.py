# Kompletna lista preseta
_PRESETS = [
    { # 0
        'index': 0,
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.5, 'newSymbols': 'F[+F]F[-F]G'},
            {'symbol': 'F', 'odds': 0.5, 'newSymbols': 'F[+F]G'},
            {'symbol': 'G', 'odds': 0.7, 'newSymbols': 'GG'},
            {'symbol': 'G', 'odds': 0.3, 'newSymbols': '[+F-G-F][++GZ]'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[-F++F-Z][+F-Z]'},
        ]
    },
    { #1
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'F[+FG]F[-FG]G'},
            {'symbol': 'G', 'odds': 0.6, 'newSymbols': 'G[+Z][--Z]F'},
            {'symbol': 'G', 'odds': 0.4, 'newSymbols': 'G[-Z][++Z]F'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[+FZ][-FZ]G'},
        ]
    },
    { #2
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.33, 'newSymbols': 'F[+F]F[-F][F]G'},
            {'symbol': 'F', 'odds': 0.33, 'newSymbols': 'F[+F][F]G'},
            {'symbol': 'F', 'odds': 0.34, 'newSymbols': 'F[-F][F]G'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'FF[+GZ++G-F[+GZ]][-G++F-G]'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[+F-G-F][++GZ]'},
            ]
    },
    { #3
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.33, 'newSymbols': 'F[+F]F[-F]F'},
            {'symbol': 'F', 'odds': 0.33, 'newSymbols': 'F[+F]F'},
            {'symbol': 'F', 'odds': 0.34, 'newSymbols': 'F[-F]F'},
        ]
    },
    { #4
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'F+[-F-GF-G][+FF][--GF[+G]][++F-G]'},
        ]
    },
    { #5
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FG[FG[+GF]]'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'FF[+GZ++G-F[+GZ]][-G++F-G]'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[+F-G-F][++GZ]'},
        ]
    },
    { #6
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'F[+F]F[-F]F'},
        ]
    },
    { #7
        'axiom': 'G',
        'rules': [
            {'symbol': 'G', 'odds': 0.33, 'newSymbols': 'F[+G]F[-G]+G'},
            {'symbol': 'G', 'odds': 0.33, 'newSymbols': 'F[-G]F[-G]+G'},
            {'symbol': 'G', 'odds': 0.34, 'newSymbols': 'F[-G]F+G'},
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
        ]
    },
    { #8
        'axiom': 'G',
        'rules': [
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'F[-[[G]+G]]+F[+FG]-G'},
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
        ]
    },
    { #9
        'axiom': 'F',
        'rules' : [
             {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF-[-F+F+F]+[+F-F-F]'},
        ]
    },
    { #10
        'axiom': 'X', 
        'rules' : [
             {'symbol': 'X', 'odds': 1.0, 'newSymbols': 'F[+X]F[-X]+X'},
             {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'}
        ]
    },
    { #11
        'axiom': 'X', 
        'rules' : [
             {'symbol': 'X', 'odds': 1.0, 'newSymbols': 'F-[[X]+X]+F[+FX]-X'},
             {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'}
        ]
    }
]
