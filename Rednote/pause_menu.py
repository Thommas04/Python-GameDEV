
# REDNOTE - PAUSE MENU
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] #

from ursina import *
from functions import fileread
from direct.filter.CommonFilters import CommonFilters
from time import *

pausemenu_bg = 'menu/pause_menu/backgrounds/pause_menu_bg.png'

pause_menu_opened = False
game_blured = False


class PauseMenu(Entity):
    def __init__(self, language_file):
        global filters
        self.language_file = language_file
        self.pause_menu_bg = Entity(texture=pausemenu_bg, alpha=0, scale=(0.68, 1.08, 0), position=[-2, -0.040, 0], model='quad', collider='box', parent=camera.ui)

        self.filters = CommonFilters(base.win, base.cam)
        self.filters.setBlurSharpen(amount=0)
        self.filters.setBlurSharpen(amount=1)

    def show_menu(self):
        global pause_menu_opened
        self.filters.setBlurSharpen(amount=0)
        pause_menu_opened = True

        self.pause_menu_bg.animate_position([-0.55, -0.040, 0], curve=curve.linear, duration=0.3, delay=0.01)
        self.pause_menu_bg.fade_in(value=1, duration=0.3, delay = 0.01)


    def close_menu(self):
        global pause_menu_opened
        self.filters.setBlurSharpen(amount=1)
        pause_menu_opened = False

        self.pause_menu_bg.fade_in(value=0, duration=0.25, delay = 0.01)
        self.pause_menu_bg.animate_position([-2, -0.040, 0], curve=curve.in_quart, duration=0.25, delay=0.01)



