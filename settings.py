from typing import Union

# Deafult
SIZE = (1106, 750)
TITLE = 'AntiAFK'

COLORS = {
    'BG0': '#000924',
    'BG1': '#041b38',
    'BG2': '#093659',
    'BG3': '#145d87',
    'BG4': '#228399',
    'FG0': '#31b0b0',
    'FG1': '#46cfb3',  # TXT0
    'FG2': '#73f0c6',  # TXT1
    'FG3': '#abffd1',
    'FG4': '#d9ffe2'
}

FONT = 'Arial'

# Top segment
TOP = {
    'BG': 'transparent',

    'FILEPATCH': {
        'BG': COLORS['BG1'],
        'CORNERRADIUS': 15,

        'PATCH': {
            'BG': COLORS['BG1'],
            'TXTCOL': COLORS['FG1'],
            'BORDERWIDTH': 0,
            'FONT': (FONT, 30),

            'BUTTON': {
                'CORNERRADIUS': 10,
                'FONT': (FONT, 40),
                'BG': COLORS['BG3'],
                'TXTCOL': COLORS['FG2']
            }
        },
    },

    'ONOFFBUTTON': {
        'IMGSIZE': (60, 60),
        'CORNERRADIUS': 30,
        'TXTCOL': COLORS['FG2'],

        'OFF': {
            'BG': COLORS['BG3'],
            'HOVER': COLORS['BG3']
        },

        'ON': {
            'BG': COLORS['FG3'],
            'HOVER': COLORS['FG3']
        }
    },

    'ONOFFKEY': {
        'CORNERRADIUS': 15,
        'BG': COLORS['BG2'],
        'HOVER': COLORS['BG1'],
        'FONT': (FONT, 30),
        'TXTCOL': COLORS['FG1']
    },

    'STICKBOTTOMTXTFRAME': {
        'BG': 'transparent',
        'TXTCOL': COLORS['FG1'],

        'SETTING': {
            'FONT': (FONT, 40),
            'PADX': 15
        },

        'ONOFFKEY': {
            'FONT': (FONT, 40),
            'PADX': 0
        },
    }
}

# Middle segment
MID = {
    'BG': 'transparent',

    'OPTION': {
        'CORNERRADIUS': 30,
        'IMGSIZE': (90, 90),

        'OFF': {
            'BG': COLORS['BG3'],
            'HOVER': COLORS['BG2']
        },

        'ON': {
            'BG': COLORS['FG3'],
            'HOVER': COLORS['FG2']
        }
    }
}

# Bottom segment
BOTTOM = {
    'BG': 'transparent',
    'PADY': 5,
    'SWITCHER': {
        'BG': 'transparent',
        'LABEL': {
            'BG': COLORS['BG1'],
            'TXTCOL': COLORS['FG1'],
            'CORNERRADIUS': 10,
        },
        'BUTTON': {
            'BG': COLORS['BG2'],
            'HOVER': COLORS['BG1'],
            'TXTCOL': COLORS['FG1'],
            'CORNERRADIUS': 10,
        },
        'DIALOGBOX': {
            'BG': COLORS['BG0'],
            'BUTTON': {
                'BG': COLORS['FG1'],
                'HOVER': COLORS['FG2'],
                'TXT': COLORS['BG2']
            },
            'ENTRY': {
                'BG': COLORS['BG2'],
                'TXT': COLORS['FG3'],
                'BORDER': COLORS['BG3']
            },

            'VARTXT': {
                'TIMES': 'ilość ruchów >=0',
            }
        }
    }
}


class Variables():
    def __init__(self):
        pass

    def Deafult(self, name: str) -> Union[str, int, tuple]:
        match name:
            case 'TIMES':
                return 5
            case 'TIME':
                return 10
            case 'TIMECOOLDOWN':
                return 100
            case 'RESETTIME':
                return 20
            case 'RESETTIMERAND':
                return 10
            case 'FPS':
                return 60
            case 'RANGE':
                return 100
            case 'RANDOMNESS':
                return 100
            case 'MOUSEMODE':
                return (1, 0)
            case 'CLICKNUMBER':
                return 1
            case 'COOLDOWN':
                return 10
            case 'KEYBOARDIF':
                return 0
            case 'KEYS':
                return 'w+s+a+d'
            case 'INITIALCOOLDOWN':
                return 7
            case 'LOOKINGFORKEYS':
                return 'f7'

    def Explanations(self, name: str) -> str:
        match name:
            case 'TIMES':
                return 'How many times events happen in one loop iteration'
            case 'TIME':
                return 'Time of singular event'
            case 'TIMECOOLDOWN':
                return 'Time between singular events'
            case 'RESETTIME':
                return 'Time between loop iterations'
            case 'RESETTIMERAND':
                return 'Randomness of time between loop iterations (Range around ResetTime)'
            case 'FPS':
                return 'In how many FPS mouse will move'
            case 'RANGE':
                return 'Distance of singular mouse move'
            case 'RANDOMNESS':
                return 'Randomness of distance that mouse cover in singular move (Range around Range)'
            case 'MOUSEMODE':
                # Later
                return '(ruch,przycisk) (0-nic 1-ruch, 0-nic 1-LMB 2-RMB 3-BMB)'
            case 'CLICKNUMBER':
                return 'How many clicks per event'
            case 'COOLDOWN':
                return 'Time between interactions'
            case 'KEYBOARDIF':
                return 'czy włączać klawiature'  # Later
            case 'KEYS':
                return 'Keys that have a chance to be clicked per event'
            case 'INITIALCOOLDOWN':
                return 'Initial cooldown (when turining ON whole script)'
            case 'LOOKINGFORKEYS':
                return 'przycisk ON/OFF'  # Later

    def Requirements(self, name: str) -> str:
        # Z = "\u2124"
        # N = "\u2115"
        # R = "\u211D"
        # Ele. of = "\u2208"
        match name:
            case 'TIMES':
                return 'x \u2208 \u2115+'
            case 'TIME':
                return 'x \u2208 \u211D (ms)'
            case 'TIMECOOLDOWN':
                return 'x \u2208 \u211D (ms)'
            case 'RESETTIME':
                return 'x \u2208 \u211D (s)'
            case 'RESETTIMERAND':
                return 'x \u2208 \u2115 (s) (0 also)'
            case 'FPS':
                return 'x \u2208 \u2115+'
            case 'RANGE':
                return 'x \u2208 \u2115 (px) (0 also)'
            case 'RANDOMNESS':
                return 'x \u2208 \u2115+ (px)'
            case 'MOUSEMODE':
                # Later
                return '(ruch,przycisk) (0-nic 1-ruch, 0-nic 1-LMB 2-RMB 3-BMB)'
            case 'CLICKNUMBER':
                return 'x \u2208 \u2115 (0 also)'
            case 'COOLDOWN':
                return 'x \u2208 \u211D (px)'
            case 'KEYBOARDIF':
                return 'czy włączać klawiature'  # Later
            case 'KEYS':
                return 'Button "+" Button'  # Later
            case 'INITIALCOOLDOWN':
                return 'x \u2208 \u211D (s)'
            case 'LOOKINGFORKEYS':
                return 'przycisk ON/OFF'  # Later


# Others
OTHERS = {
    'CHANGEKEY': {
        'BG': 'black',
        'FONT0': (FONT, 30),
        'FONT1': (FONT, 50),
        'TXTCOL': 'white'
    }
}


# Img
IMAGES = {
    'KEYBOARD0': 'Img/keyboard0.png',
    'KEYBOARD1': 'Img/keyboard1.png',
    'MOUSEMOVE0': 'Img/mouse0.png',
    'MOUSEMOVE1': 'Img/mouse1.png',
    'MOUSEBUTTON0': 'Img/mouse0.png',
    'MOUSEBUTTON1': 'Img/left-click1.png',
    'MOUSEBUTTON2': 'Img/right-click2.png',
    'MOUSEBUTTON3': 'Img/both-click3.png',
    'ONOFFBUTTON0': 'Img/on-off-button0.png',
    'ONOFFBUTTON1': 'Img/on-off-button1.png',
    'ICON': 'Img/mouse.ico'
}


if __name__ == '__main__':
    v = Variables()
    x = ['TIMES', 'TIME', 'TIMECOOLDOWN', 'RESETTIME', 'RESETTIMERAND', 'FPS', 'RANGE', 'RANDOMNESS',
         'MOUSEMODE', 'CLICKNUMBER', 'COOLDOWN', 'KEYBOARDIF', 'KEYS', 'INITIALCOOLDOWN', 'LOOKINGFORKEYS']
    for i in x:
        print(f'{i} = {v.Explanations(i)} - {v.Requirements(i)}')
