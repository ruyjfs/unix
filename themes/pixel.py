# these symbols for now have to be set directly in powerline-shell.py:
class Powerline:
    symbols = {
        # Pixel
         'patched': {
            'lock': u'\uE0A2',
            'network': u'\uE0A2',
            'separator': u'\uE0C6',
            'separator_thin': u'\uE0C6'
        }
    }

# flame colors (Work in progress)!
from powerline_shell.themes.default import DefaultColor

class Color(DefaultColor):
    USERNAME_FG = 250
