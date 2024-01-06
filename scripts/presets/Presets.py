# Kompletna lista preseta
_PRESETS = [
    {
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 0.5, 'newSymbols': 'F[+F]F[-F]G'},
            {'symbol': 'F', 'odds': 0.5, 'newSymbols': 'F[+F]G'},
            {'symbol': 'G', 'odds': 0.7, 'newSymbols': 'GG'},
            {'symbol': 'G', 'odds': 0.3, 'newSymbols': '[+F-G-F][++GZ]'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[-F++F-Z][+F-Z]'},
        ]
    },
    {
        'axiom': 'F',
        'rules': [
            {'symbol': 'F', 'odds': 1.0, 'newSymbols': 'F[+FG]F[-FG]G'},
            {'symbol': 'G', 'odds': 0.6, 'newSymbols': 'G[+Z][--Z]F'},
            {'symbol': 'G', 'odds': 0.4, 'newSymbols': 'G[-Z][++Z]F'},
            {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[+FZ][-FZ]G'},
        ]
    },
    {
    'axiom': 'F',
    'rules': [
        {'symbol': 'F', 'odds': 0.33, 'newSymbols': 'F[+F]F[-F][F]G'},
        {'symbol': 'F', 'odds': 0.33, 'newSymbols': 'F[+F][F]G'},
        {'symbol': 'F', 'odds': 0.34, 'newSymbols': 'F[-F][F]G'},
        {'symbol': 'G', 'odds': 1.0, 'newSymbols': 'FF[+GZ++G-F[+GZ]][-G++F-G]'},
        {'symbol': 'Z', 'odds': 1.0, 'newSymbols': '[+F-G-F][++GZ]'},
        ]
    },
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
