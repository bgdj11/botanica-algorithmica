# Kompletna lista preseta
_PRESETS = [
    { #1
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
    { #2
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'F[+FG]F[-FG]G'},
            {'symbol': 'G', 'odds': 0.6, 'newSymbols': 'G[+Z][--Z]F'},
            {'symbol': 'G', 'odds': 0.4, 'newSymbols': 'G[-Z][++Z]F'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[+FZ][-FZ]G'},
        ]
    },
    { #3
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.33, 'newSymbols': 'F[+F]F[-F][F]G'},
            {'symbol': 'F', 'odds': 0.33, 'newSymbols': 'F[+F][F]G'},
            {'symbol': 'F', 'odds': 0.34, 'newSymbols': 'F[-F][F]G'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'FF[+GZ++G-F[+GZ]][-G++F-G]'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[+F-G-F][++GZ]'},
            ]
    },
    { #4
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.33, 'newSymbols': 'F[+F]F[-F]F'},
            {'symbol': 'F', 'odds': 0.33, 'newSymbols': 'F[+F]F'},
            {'symbol': 'F', 'odds': 0.34, 'newSymbols': 'F[-F]F'},
        ]
    },
    { #5
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'F+[-F-GF-G][+FF][--GF[+G]][++F-G]'},
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
    },
    { # 12 
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.6, 'newSymbols': 'F[+F]F[-F][G]'},
            {'symbol': 'F', 'odds': 0.4, 'newSymbols': 'F[-F]F[+F][Z]'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'GG'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[+F-Z][-F+Z]'},
        ]
    },
    { # 13
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.5, 'newSymbols': 'F[+F]G[-F][F]Z'},
            {'symbol': 'F', 'odds': 0.5, 'newSymbols': 'F[-F][G]F'},
            {'symbol': 'G', 'odds': 0.8, 'newSymbols': 'GG'},
            {'symbol': 'G', 'odds': 0.2, 'newSymbols': '[Z][+G]'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[-G+Z]'},
        ]
    },
    { # 14  
        'axiom': 'G',
        'rules': [
            {'symbol': 'G', 'odds': 0.6, 'newSymbols': 'G[+G]F[-G]Z'},
            {'symbol': 'G', 'odds': 0.4, 'newSymbols': 'G[-G]F[+G]Z'},
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[+F-G]Z'},
        ]
    },
    { # 15
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.8, 'newSymbols': 'F[+G]F[-G][Z]'},
            {'symbol': 'F', 'odds': 0.2, 'newSymbols': 'F[-G]F[+G][Z]'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'G[+F][-F]G'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': 'Z[+F][-F]Z'},
        ]
    },
    { # 16
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF-[-F+G+F]+[+F-G-F]'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': '[+G]F[-G]'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[+Z][-Z]'},
        ]
    },
    { # 17
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'F[+FG]F[-FG]'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'G[-F][+F]Z'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': 'Z[+Z]Z[-Z]'},
        ]
    },
    { # 18
        'axiom': 'G',
        'rules': [
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'G[+F]G[-F][+G]'},
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'F[+F]F[-F]'},
        ]
    },
    { # 19
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.7, 'newSymbols': 'F[+F]F[-F][+F]G'},
            {'symbol': 'F', 'odds': 0.3, 'newSymbols': 'F[-F]F[+F][+F]Z'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'G[+G]G'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': 'Z[+Z][-Z]'},
        ]
    },
    { # 20
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.7, 'newSymbols': 'F[+FG]F[-FG][+F]'},
            {'symbol': 'F', 'odds': 0.3, 'newSymbols': 'F[-FG]F[+FG][-F]Z'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'G[+G]G[-G]'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': 'Z[+Z]Z[-Z]'},
        ]
    },
    { # 21
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.6, 'newSymbols': 'F[+F]F[-F][G]Z'},
            {'symbol': 'F', 'odds': 0.4, 'newSymbols': 'F[-F]F[+F]Z'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'G[+G][-G]'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': 'Z[+Z]Z[-Z]'},
        ]
    },
    { # 22
        'axiom': 'G',
        'rules': [
            {'symbol': 'G', 'odds': 0.7, 'newSymbols': 'G[+G]F[-G]Z'},
            {'symbol': 'G', 'odds': 0.3, 'newSymbols': 'G[-G]F[+G]Z'},
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[Z]'},
        ]
    },
    { # 23
    'axiom': 'X',
        'rules': [
            {'symbol': 'X', 'odds': 0.6, 'newSymbols': 'X[+F]X[-F]G'},
            {'symbol': 'X', 'odds': 0.4, 'newSymbols': 'X[-F]X[+F][Z]'},
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'F[+F]F[-F]'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'GG'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': 'Z[+Z][-Z]'},
        ]
    },
    { # 24
        'axiom': 'Z',
        'rules': [
            {'symbol': 'Z', 'odds': 0.5, 'newSymbols': 'Z[+F]Z[-F]G'},
            {'symbol': 'Z', 'odds': 0.5, 'newSymbols': 'Z[-F]Z[+F][G]'},
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'F[+F]F[-F]'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'GG[+G][-G]'},
        ]
    },
    { # 25
        'axiom': 'X',
        'rules': [
            {'symbol': 'X', 'odds': 0.7, 'newSymbols': 'X[+F]X[-F]G'},
            {'symbol': 'X', 'odds': 0.3, 'newSymbols': 'X[-F]X[+F][Z]'},
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF[+F][-F]'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'GG'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[Z][+Z][-Z]'},
        ]
    },
    { # 26
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'F[+F-GF-G][--F+G]F[+FF]'},
        ]
    },
    { # 27
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.5, 'newSymbols': 'F[+FF]F[-FF]G'},
            {'symbol': 'F', 'odds': 0.5, 'newSymbols': 'F[+F]G'},
            {'symbol': 'G', 'odds': 0.7, 'newSymbols': 'GG'},
            {'symbol': 'G', 'odds': 0.3, 'newSymbols': '[+G-FG][--GZ]'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[-F+G-Z][+F-Z]'},
        ]
    },
    { # 28
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'F[+G-FG][-G+F]G[+FF]'},
        ]
    },
    { # 29
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.6, 'newSymbols': 'FF-[-F+F+F]+[+F-F-F]G'},
            {'symbol': 'F', 'odds': 0.4, 'newSymbols': 'F[-F]F[+F]G'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': '[+G][-G]'},
        ]
    },
    { # 30
        'axiom': 'X',
        'rules': [
            {'symbol': 'X', 'odds': 0.7, 'newSymbols': 'F-[[X]+X]+F[+FX]-X'},
            {'symbol': 'X', 'odds': 0.3, 'newSymbols': 'F[+X]F[-X]+X'},
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
        ]
    },
    { # 31
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'F[+FG]F[-FG]'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'G[-F][+F]Z'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[+FZ][-FZ]G'},
        ]
    },
    { # 32
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'F[+GF-G][--F+G]F'},
        ]
    },
    { # 33
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.4, 'newSymbols': 'F[+FF]F[-F]G'},
            {'symbol': 'F', 'odds': 0.6, 'newSymbols': 'F[-F][+F]G'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': '[+G][-G]G'},
        ]
    },
    { # 34
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF[+F][-F]'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'G[+G-FG][-G]F'},
        ]
    },
    { # 35
        'axiom': 'X',
        'rules': [
            {'symbol': 'X', 'odds': 0.6, 'newSymbols': 'F[+X]F[-X][G]'},
            {'symbol': 'X', 'odds': 0.4, 'newSymbols': 'F[-X][+X]G'},
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': '[+G][-G]'},
        ]
    },
    { # 36
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'F[+G]F[-G][++G][--G]G'},
        ]
    },
    { # 37
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'F[+G-F-G][--F+G+F]G'},
        ]
    },
    { # 38
        'axiom': 'G',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'FF[+F][-F]G'},
            {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'G[+F-G-F][--F+G+F]G'},
        ]
    }

]
