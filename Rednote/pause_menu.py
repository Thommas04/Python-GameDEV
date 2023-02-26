
# REDNOTE - PAUSE MENU
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] #

from ursina import *
from functions import fileread
from direct.filter.CommonFilters import CommonFilters
from time import *
from random import *

from pynput.keyboard import Key, Controller

pausemenu_bg = 'menu/pause_menu/backgrounds/pause_menu_bg.png'

# CLOCK

clock_hours_spritesheet = 'menu/pause_menu/clock/clock_hours_sheet.png'
clock_minutes_spritesheet = 'menu/pause_menu/clock/clock_minutes_sheet.png'
pocketwatch_bg = 'menu/pause_menu/clock/pocketwatch.png'


# --------------------------------------------

pause_menu_opened = False
game_blured = False
paused = False

keyboard = Controller()

def get_pausemenu_state():
    return paused

class PauseMenu(Entity):
    def anim_clock(self, mins, hrs):

        if mins == 0:
            self.hours_efix = 0
        if mins == 15:
            self.hours_efix = 1
        if mins == 30:
            self.hours_efix = 2
        if mins == 45:
            self.hours_efix = 3

        hours = (hrs * 4) + self.hours_efix

        self.hours_spritesheet.tile_coordinate = [hours, 0]
        self.minutes_spritesheet.tile_coordinate = [mins , 0]

        print('megyek')

    # ///////////////////////////////////////////////////

    def resume(self):
        self.player.pause_menu_state = None
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)

    def open_map(self):
        pass

    def open_story(self):
        self.player.pause_menu_state = 'story'

        keyboard.press(Key.esc)
        keyboard.release(Key.esc)

        self.main_menu.show_story_menu()


    def open_help(self):
        pass

    def open_settings(self):
        pass

    def open_quit(self):

        # Ha beállítok egy rákérdező / beleegyező menüt, hogy valóban ki szeretne-e lépni akkor ezt másképp kell majd orientálni
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)

        self.main_menu.start_sound()
        self.main_menu.show_menu()
        self.hud.hide_hud()
        self.hud.hide_attack_hud()
        self.main_menu.canvas.fade_in(value = 1, duration = 0.4)
        self.main_menu.canvasbg.fade_in(value = 1, duration = 0.4)

    # -----------------------

    def on_hover(self, ref):
        if ref == self.quit_txt:
            ref.color = rgb(255, 103, 109)
        else:
            ref.color = color.white

    def on_leave(self, ref):
        ref.color = color.black

    # -----------------------

    def __init__(self, language_file, main_menu, hud, player):
        global filters
        self.main_menu = main_menu
        self.hud = hud
        self.language_file = language_file
        self.pause_menu_bg = Entity(texture=pausemenu_bg, alpha=0, scale=(0.68, 1.08, -0.12), position=[-2, -0.040, 0], model='quad', parent=camera.ui)
        self.player = player

        self.hours_efix = 0

        self.filters = CommonFilters(base.win, base.cam)
        self.filters.setBlurSharpen(amount=0)
        self.filters.setBlurSharpen(amount=1)

        ################################################################################################################
        # INIT TEXTS Handling ------------------------------------------------------------------------------------------

        self.resume_txt = Text(text="", rotation = (0, 0, -6), position = [-2, 0, -0.13], origin=(0,0),color=color.black, parent=camera.ui, font='fonts/CHINESER.TTF', scale = 2.1)
        self.map_txt = Text(text="", rotation=(0, 0, -6), position = [-2, -0.08, -0.13], origin=(0,0),color=color.black, parent=camera.ui, font='fonts/CHINESER.TTF', scale=2.1)
        self.story_txt = Text(text="", rotation=(0, 0, -6), position = [-2, -0.16, -0.13], origin=(0,0),color=color.black, parent=camera.ui, font='fonts/CHINESER.TTF', scale=2.1)
        self.help_txt = Text(text="", rotation=(0, 0, -6), position = [-2, -0.24, -0.13], origin=(0,0),color=color.black, parent=camera.ui,font='fonts/CHINESER.TTF', scale=2.1)
        self.settings_txt = Text(text="", rotation=(0, 0, -6), position = [-2, -0.32, -0.13], origin=(0,0),color=color.black, parent=camera.ui,font='fonts/CHINESER.TTF', scale=2.1)
        self.quit_txt = Text(text="", rotation=(0, 0, -6), position = [-2, -0.4, -0.13], origin=(0,0),color=color.black, parent=camera.ui, font='fonts/CHINESER.TTF', scale=2.1)

        self.resume_click = Entity(alpha = 0, rotation = (0, 0, -6), scale=(0, 0.065, -0.12), origin=(0,0), position = self.resume_txt.position, model='quad', collider='box', parent=camera.ui, on_click=Func(PauseMenu.resume, self), on_mouse_enter=Func(PauseMenu.on_hover, self, self.resume_txt), on_mouse_exit=Func(PauseMenu.on_leave, self, self.resume_txt))
        self.map_click = Entity(alpha = 0, rotation=(0, 0, -6), scale=(0.2, 0.065, -0.12), origin=(0, 0), position=self.map_txt.position, model='quad', collider='box', parent=camera.ui, on_click=Func(PauseMenu.open_map, self), on_mouse_enter=Func(PauseMenu.on_hover, self, self.map_txt), on_mouse_exit=Func(PauseMenu.on_leave, self, self.map_txt))
        self.story_click = Entity(alpha = 0, rotation=(0, 0, -6), scale=(0.2, 0.065, -0.12), origin=(0, 0), position=self.story_txt.position, model='quad', collider='box', parent=camera.ui, on_click=Func(PauseMenu.open_story, self), on_mouse_enter=Func(PauseMenu.on_hover, self, self.story_txt), on_mouse_exit=Func(PauseMenu.on_leave, self, self.story_txt))
        self.help_click = Entity(alpha = 0, rotation=(0, 0, -6), scale=(0.2, 0.065, -0.12), origin=(0, 0), position=self.help_txt.position, model='quad', collider='box', parent=camera.ui, on_click=Func(PauseMenu.open_help, self), on_mouse_enter=Func(PauseMenu.on_hover, self, self.help_txt), on_mouse_exit=Func(PauseMenu.on_leave, self, self.help_txt))
        self.settings_click = Entity(alpha = 0, rotation=(0, 0, -6), scale=(0.2, 0.065, -0.12), origin=(0, 0), position=self.settings_txt.position, model='quad', collider='box', parent=camera.ui, on_click=Func(PauseMenu.open_settings, self), on_mouse_enter=Func(PauseMenu.on_hover, self, self.settings_txt), on_mouse_exit=Func(PauseMenu.on_leave, self, self.settings_txt))
        self.quit_click = Entity(alpha = 0, rotation=(0, 0, -6), scale=(0.2, 0.065, -0.12), origin=(0, 0), position=self.quit_txt.position, model='quad', collider='box', parent=camera.ui, on_click=Func(PauseMenu.open_quit, self), on_mouse_enter=Func(PauseMenu.on_hover, self, self.quit_txt), on_mouse_exit=Func(PauseMenu.on_leave, self, self.quit_txt))

        ################################################################################################################
        # POCKET WATCH ------------------------------------------------------------------------------------------

        self.pocket_watch_bg = Entity(texture = pocketwatch_bg, model = 'quad', position = (-0.72, 0.35, -0.1), scale = (0.3, 0.3, 0), alpha = 0, parent = camera.ui)

        self.hours_spritesheet = Entity(texture = clock_hours_spritesheet, model = 'quad', position = (self.pocket_watch_bg.position.x - 0.005, self.pocket_watch_bg.position.y - 0.025, -0.2), scale=(0.11, 0.11, 0), alpha = 0, parent = camera.ui, tileset_size=[48, 1], tile_coordinate = [25, 0])
        self.minutes_spritesheet = Entity(texture = clock_minutes_spritesheet, model = 'quad', position = (self.pocket_watch_bg.position.x - 0.005, self.pocket_watch_bg.position.y - 0.025, -0.2), scale=(0.16, 0.16, 0), alpha = 0, parent = camera.ui, tileset_size=[60, 1], tile_coordinate = [15, 0])

    # Menü kinyitása
    def show_menu(self):
        global pause_menu_opened, paused

        pause_menu_opened = True
        paused = True

        self.pause_menu_bg.animate_position([-0.55, -0.040, 0], curve=curve.linear, duration=0.3, delay=0.01)
        self.pause_menu_bg.fade_in(value=0.9, duration=0.3, delay = 0.01)

        self.pocket_watch_bg.fade_in(value=0.7, duration=0.3, delay = 0.01)
        self.hours_spritesheet.fade_in(value=0.9, duration=0.3, delay = 0.01)
        self.minutes_spritesheet.fade_in(value=0.9, duration=0.3, delay=0.01)

        ################################################################################################################
        # SHOW TEXTS Handling ------------------------------------------------------------------------------------------

        a, b = 660, 750
        random_resume_x = (randint(a, b) / 1000) * -1
        random_map_x = (randint(a, b) / 1000) * -1
        random_story_x = (randint(a, b) / 1000) * -1
        random_help_x = (randint(a, b) / 1000) * -1
        random_settings_x = (randint(a, b) / 1000) * -1
        random_quit_x = (randint(a, b) / 1000) * -1

        self.resume_txt.animate_position([random_resume_x, 0, -0.01], curve=curve.linear, duration=0.2, delay = 0.04)
        self.map_txt.animate_position([random_map_x, -0.08, -0.01], curve=curve.linear, duration=0.2, delay = 0.04)
        self.story_txt.animate_position([random_story_x, -0.16, -0.01], curve=curve.linear, duration=0.2, delay = 0.04)
        self.help_txt.animate_position([random_help_x, -0.24, -0.01], curve=curve.linear, duration=0.2, delay = 0.04)
        self.settings_txt.animate_position([random_settings_x, -0.32, -0.01], curve=curve.linear, duration=0.12, delay = 0)
        self.quit_txt.animate_position([random_quit_x, -0.4, -0.01], curve=curve.linear, duration=0.2, delay = 0.04)

        self.resume_txt.text = self.language_file[1].get('Resume')
        self.map_txt.text = self.language_file[1].get('Map')
        self.story_txt.text = self.language_file[1].get('Story')
        self.help_txt.text = self.language_file[1].get('Help')
        self.settings_txt.text = self.language_file[1].get('Settings')
        self.quit_txt.text = self.language_file[1].get('Quit')

        ## ------- ##

        self.resume_click.animate_position([random_resume_x, 0, -0.02], curve = curve.linear, duration = 0.2, delay = 0.01)
        self.map_click.animate_position([random_map_x, -0.08, -0.02], curve = curve.linear, duration = 0.2, delay = 0.01)
        self.story_click.animate_position([random_story_x, -0.16, -0.02], curve = curve.linear, duration = 0.2, delay = 0.01)
        self.help_click.animate_position([random_help_x, -0.24, -0.02], curve = curve.linear, duration = 0.2, delay = 0.01)
        self.settings_click.animate_position([random_settings_x, -0.32, -0.02], curve = curve.linear, duration = 0.2, delay = 0.01)
        self.quit_click.animate_position([random_quit_x, -0.4, -0.02], curve = curve.linear, duration = 0.2, delay = 0.01)

        self.resume_click.scale=(Text.get_width(self.resume_txt.text) * 2.5, 0.065, 0)
        self.map_click.scale = (Text.get_width(self.map_txt.text) * 2.5, 0.065, 0)
        self.story_click.scale = (Text.get_width(self.story_txt.text) * 2.5, 0.065, 0)
        self.help_click.scale = (Text.get_width(self.help_txt.text) * 2.5, 0.065, 0)
        self.settings_click.scale = (Text.get_width(self.settings_txt.text) * 2.5, 0.065, 0)
        self.quit_click.scale = (Text.get_width(self.quit_txt.text) * 2.5, 0.065, 0)

        self.hud.hide_hud()
        self.filters.setBlurSharpen(amount = 0)


    # Menü bezárása
    def close_menu(self, state):
        global pause_menu_opened, paused
        self.filters.setBlurSharpen(amount=1)
        pause_menu_opened = False
        paused = False

        self.pause_menu_bg.fade_in(value=0, duration=0.25, delay = 0.01)
        self.pause_menu_bg.animate_position([-2, -0.040, 0], curve=curve.in_quart, duration=0.25, delay=0.01)

        self.pocket_watch_bg.fade_in(value=0, duration=0.1, delay=0.01)
        self.hours_spritesheet.fade_in(value=0, duration=0.1, delay=0.01)
        self.minutes_spritesheet.fade_in(value=0, duration=0.1, delay=0.01)

        ################################################################################################################
        # HIDE TEXTS Handling ------------------------------------------------------------------------------------------

        self.resume_txt.animate_position([-2, 0, -0.01], curve=curve.linear, duration=0.2, delay=0.01)
        self.map_txt.animate_position([-2, -0.08, -0.01], curve=curve.linear, duration=0.2, delay=0.01)
        self.story_txt.animate_position([-2, -0.16, -0.01], curve=curve.linear, duration=0.2, delay=0.01)
        self.help_txt.animate_position([-2, -0.24, -0.01], curve=curve.linear, duration=0.2, delay=0.01)
        self.settings_txt.animate_position([-2, -0.32, -0.01], curve=curve.linear, duration=0.2, delay=0.01)
        self.quit_txt.animate_position([-2, -0.4, -0.01], curve=curve.linear, duration=0.2, delay=0.01)

        self.resume_click.animate_position([-2, 0, -0.02], curve=curve.linear, duration=0.2, delay=0.01)
        self.map_click.animate_position([-2, -0.08, -0.02], curve=curve.linear, duration=0.2, delay=0.01)
        self.story_click.animate_position([-2, -0.16, -0.02], curve=curve.linear, duration=0.2, delay=0.01)
        self.help_click.animate_position([-2, -0.24, -0.02], curve=curve.linear, duration=0.2, delay=0.01)
        self.settings_click.animate_position([-2, -0.32, -0.02], curve=curve.linear, duration=0.2, delay=0.01)
        self.quit_click.animate_position([-2, -0.4, -0.02], curve=curve.linear, duration=0.2, delay=0.01)

        if state == 'ingame' and self.player.builder_mode == False and self.player.pause_menu_state == None:
            self.hud.show_hud()