
from PIL import Image
from ursina import *
from functions import fileread

# menu backgrounds
morning_bg1 = 'menu/main_menu/background/menu_morning_1.png'
morning_bg2 = 'menu/main_menu/background/menu_morning_2.png'
sunset_bg1 = 'menu/main_menu/background/menu_sunset_1.png'
day_bg1 = 'menu/main_menu/background/menu_day_1.png'
day_bg2 = 'menu/main_menu/background/menu_day_2.png'

# menu letters
letter_r = 'menu/main_menu/letters/letter_r.png'
letter_e = 'menu/main_menu/letters/letter_e.png'
letter_d = 'menu/main_menu/letters/letter_d.png'
letter_n = 'menu/main_menu/letters/letter_n.png'
letter_o = 'menu/main_menu/letters/letter_o.png'
letter_t = 'menu/main_menu/letters/letter_t.png'

# menu shadows
right_down_shadow = 'menu/main_menu/shadows/menu_shadow.png'
noise = 'menu/main_menu/shadows/menu_noise.png'
menu_splitter = 'menu/main_menu/shadows/menu_splitter.png'

# menu buttons
loadbar_deactive = 'menu/main_menu/shadows/load_bar_deactive.png'
loadbar_active = 'menu/main_menu/shadows/load_bar_active.png'
loadbar_selected = 'menu/main_menu/shadows/load_bar_selected.png'

load_infobg = 'menu/main_menu/shadows/load_infobg.png'

# menu buttons
new_game = 'menu/main_menu/buttons/new_game.png'
load_game = 'menu/main_menu/buttons/load_game.png'
exit_game = 'menu/main_menu/buttons/exit_game.png'
new_game_highlight = 'menu/main_menu/buttons/new_game_highlight.png'
load_game_highlight = 'menu/main_menu/buttons/load_game_highlight.png'
exit_game_highlight = 'menu/main_menu/buttons/exit_game_highlight.png'

loads_list = []
enable_bit = True

def enable():
    global enable_bit
    enable_bit = True

def show_outside_init():
    global infobg, menu_loadbar_pressed, load_info_list, title_txt, date_txt, usrname_label, ingame_date_label, wealth_label, creation_date_label, \
        playtime_label, cheats_label, mission_description_label,username_txt, ingame_date_txt, wealth_txt, creation_date_txt, playtime_txt, cheats_txt, description_text
    infobg = Entity(texture=load_infobg, alpha=1, model='quad', scale=(0.53, 0.75, 0), position=[-2, 0, 0], parent=camera.ui)
    menu_loadbar_pressed = False

    title_txt = Text(text="", position=[-0.77, 0.33, -0.01], color = rgb(255, 255, 255), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.75, 1.45, 0])
    date_txt = Text(text="", position=[-0.77, 0.28, -0.01], color = rgb(100, 100, 100), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.15, 0.85, 0])

    usrname_label = Text(text="", position=[-0.77, 0.22, -0.01], color = rgb(180, 180, 180), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.15, 0.85, 0])
    ingame_date_label = Text(text="", position=[-0.77, 0.18, -0.01], color = rgb(180, 180, 180), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.15, 0.85, 0])
    wealth_label = Text(text="", position=[-0.77, 0.14, -0.01], color = rgb(180, 180, 180), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.15, 0.85, 0])

    creation_date_label = Text(text="", position=[-0.77, 0.08, -0.01], color = rgb(180, 180, 180), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.15, 0.85, 0])
    playtime_label = Text(text="", position=[-0.77, 0.04, -0.01], color = rgb(180, 180, 180), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.15, 0.85, 0])
    cheats_label = Text(text="", position=[-0.77, 0, -0.01], color = rgb(236, 102, 108), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.15, 0.85, 0])
    mission_description_label = Text(text="", position=[-0.77, -0.06, -0.01], color = rgb(100, 100, 100), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.35, 1.15, 0])

    #-------------------------------------------------------------------------------------------------------------------

    username_txt = Text(text="kisposi69", position=[-0.35, 0.22, -0.01], color = rgb(165, 165, 165), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.05, 0.85, 0], origin=(0.5,0.5))
    ingame_date_txt = Text(text="Nyár 26.", position=[-0.35, 0.18, -0.01], color = rgb(165, 165, 165), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.05, 0.85, 0], origin=(0.5,0.5))
    wealth_txt = Text(text="$ 45.01", position=[-0.35, 0.14, -0.01], color = rgb(165, 165, 165), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.05, 0.85, 0], origin=(0.5,0.5))

    creation_date_txt = Text(text="20 / 04 / 10", position=[-0.35, 0.08, -0.01], color = rgb(165, 165, 165), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.05, 0.85, 0], origin=(0.5,0.5))
    playtime_txt = Text(text="26 óra", position=[-0.35, 0.04, -0.01], color = rgb(165, 165, 165), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.05, 0.85, 0], origin=(0.5,0.5))
    cheats_txt = Text(text="Engedélyezve", position=[-0.35, 0, -0.01], color = rgb(236, 102, 108), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.05, 0.85, 0], origin=(0.5,0.5))
    description_text = Text(text="Jelenj meg a temetésen!", position=[-0.77, -0.1, -0.01], color = rgb(125, 125, 125), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.15, 0.85, 0])

    load_info_list = [title_txt, date_txt, usrname_label, ingame_date_label, wealth_label, creation_date_label, playtime_label, cheats_label, mission_description_label,
                      username_txt, ingame_date_txt, wealth_txt, creation_date_txt, playtime_txt, cheats_txt, description_text]

    for objs in load_info_list:
        objs.alpha = 0



# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

def menu_play_pressed(a):
    global enable_bit
    if enable_bit == True:
        Menu.show_play_menu(a)
        Menu.hide_menu(a)
        enable_bit = False
        invoke(enable, delay = 0.9)

def menu_settings_pressed(a):
    pass
def menu_quit_pressed(a):
    global enable_bit
    if enable_bit == True:
        a.location = 'quit_main'
        Menu.hide_menu(a)
        Menu.show_exit_game(a)
        Menu.show_play_menu(a)
        a.back_fromplay.fade_in(value = 1, duration = 0.5)
        a.menu_title.animate_position([-0.75, 0.46, 0], curve=curve.linear, duration=0.4, delay=0.4)

    enable_bit = False
    invoke(enable, delay=0.9)

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

def load_game_pressed(a):
    global enable_bit
    if enable_bit == True:
        Menu.show_load_menu(a)
        Menu.hide_play_menu(a)

        enable_bit = False
        invoke(enable, delay=0.9)

def new_game_pressed(a): # NEW GAME PRESSED
    Menu.hide_play_menu(a)
    a.canvas.fade_out(value = 0, duration = 1)
    a.canvasbg.fade_out(value = 0, duration = 1)
    a.background.fade_out(value = 0, duration = 1)

def exit_game_pressed(a):
    global enable_bit
    if enable_bit == True:
        a.location = 'quit_play'
        Menu.hide_play_menu(a)
        Menu.show_exit_game(a)

        enable_bit = False
        invoke(enable, delay=0.9)

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

#ESC lenyomva - Vissza
def back_pressed(a):
    global enable_bit
    if enable_bit == True:
        if a.location == 'play':
            Menu.hide_play_menu(a)
            Menu.show_menu(a)
        if a.location == 'load':
            Menu.hide_load_menu(a)
            Menu.show_play_menu(a)
            a.menu_title.shake(duration=.25, magnitude=5, speed=.05, direction=(1, 0.5))
            a.menu_title.appear(speed=.025, delay=0.15)
        if a.location == 'quit_play':
            Menu.show_play_menu(a)
            a.menu_title.shake(duration=.25, magnitude=5, speed=.05, direction=(1, 0.5))
            a.menu_title.appear(speed=.025, delay=0.15)

        enable_bit = False
        invoke(enable, delay=0.9)

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

def menu_buttons_hovered(a):
    a.color = rgb(150, 150, 150)
def menu_buttons_exit(a):
    a.color = rgb(101, 101, 101)

######################################

def load_game_hovered(self):
    self.load_game_hightlighted.fade_in(value = 1, duration = 0)
    self.play_explaining_text.text = self.language_file[0].get('LoadInfo')
    self.load_game_text.color = rgb(236, 102, 108)
def load_game_exit(self):
    self.load_game_hightlighted.fade_out(value = 0, duration = 0)
    self.load_game_text.color = rgb(101, 101, 101)
def new_game_hovered(self):
    self.new_game_hightlighted.fade_in(value = 1, duration = 0)
    self.play_explaining_text.text = self.language_file[0].get('NewGameInfo')
    self.new_game_text.color = rgb(236, 102, 108)
def new_game_exit(self):
    self.new_game_hightlighted.fade_out(value = 0, duration = 0)
    self.new_game_text.color = rgb(101, 101, 101)
def exit_game_hovered(self):
    self.exit_game_hightlighted.fade_in(value = 1, duration = 0)
    self.play_explaining_text.text = self.language_file[0].get('QuitInfo')
    self.exit_game_text.color = rgb(236, 102, 108)
def exit_game_exit(self):
    self.exit_game_hightlighted.fade_out(value = 0, duration = 0)
    self.exit_game_text.color = rgb(101,101,101)

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

class Menu(Entity):
    def __init__(self, language_file):
        self.location = 'main'

        self.language_file = language_file

        self.pos_letters = [[-0.38, 0.35, 0],[-0.25, 0.35, 0],[-0.13, 0.35, 0],[0.01, 0.35, 0],[0.15, 0.35, 0],[0.28, 0.35, 0],[0.4, 0.35, 0]]
        self.verts = [(0, 0, 0), (2, 0, 0), (0, 1, 0), (0, 1, 0)]
        self.tris = [1, 2, 0, 2, 3, 0]
        #model = Mesh(vertices=self.verts, triangles=self.tris)

        #////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # BASE Graphics

        self.canvas = Entity(color = color.black, model= 'quad', scale=(1.920, 1.080, 0), position = [0, 0, 0.1], parent = camera.ui)
        self.canvasbg = Entity(texture = noise, model='quad', scale=(1.920, 1.080, 0), position=[0, 0, 0.08], parent=camera.ui)
        self.background = Entity(texture = morning_bg1, model='quad', scale=(1.920, 1.080, 0), position=[0, -0.0, 0], parent=camera.ui)

        # Play menüben a cím
        self.menu_title = Text(text="", position=[-2, 0.46, 0], color=rgb(126, 126, 101), parent=camera.ui,font='fonts/pricedown.otf', scale=[1.7, 1.5, 0])

        # MAIN MENU # -------------------------------------------------------------------------------------------------

        self.shadow = Entity(texture=right_down_shadow, model='quad', scale=(1, 0.1, 0), position=[0.4,-0.45,0], parent=camera.ui)

        self.r = Entity(texture=letter_r, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[0],parent=camera.ui)
        self.e1 =Entity(texture=letter_e, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[1],parent=camera.ui)
        self.d = Entity(texture=letter_d, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[2],parent=camera.ui)
        self.n = Entity(texture=letter_n, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[3],parent=camera.ui)
        self.o = Entity(texture=letter_o, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[4],parent=camera.ui)
        self.t = Entity(texture=letter_t, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[5],parent=camera.ui)
        self.e2 =Entity(texture=letter_e, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[6],parent=camera.ui)

        self.text_play = Text(text=self.language_file[0].get('Play'), position=[0.75, -0.456, -0.01], color = rgb(101, 101, 101), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.3, 1.1, 0])
        self.text_settings = Text(text=self.language_file[0].get('Settings'), position=[0.5, -0.456, -0.01], color = rgb(101, 101, 101), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.3, 1.1, 0])
        self.text_quit = Text(text=self.language_file[0].get('Quit'), position=[0.28, -0.456, -0.01], color = rgb(101, 101, 101), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.3, 1.1, 0])

        self.click_area_play = Entity(alpha = 0, scale=(0.1, 0.05, 0), position = [0.782, -0.472, 0], model= 'quad', collider = 'box', parent = camera.ui, on_click = Func(menu_play_pressed, self), on_mouse_enter = Func(menu_buttons_hovered, self.text_play), on_mouse_exit = Func(menu_buttons_exit, self.text_play))
        self.click_area_settings = Entity(alpha = 0, scale=(0.17, 0.05, 0), position = [0.57, -0.472, 0], model= 'quad', collider = 'box', parent = camera.ui, on_click = Func(menu_settings_pressed, self), on_mouse_enter = Func(menu_buttons_hovered, self.text_settings), on_mouse_exit = Func(menu_buttons_exit, self.text_settings))
        self.click_area_quit = Entity(alpha = 0, scale=(0.13, 0.05, 0), position = [0.325, -0.472, 0], model= 'quad', collider = 'box', parent = camera.ui, on_click = Func(menu_quit_pressed, self), on_mouse_enter = Func(menu_buttons_hovered, self.text_quit), on_mouse_exit = Func(menu_buttons_exit, self.text_quit))

        # Menu : Play # -------------------------------------------------------------------------------------------------
        # játék fülnél a fenti és lenti szürke vonal
        self.splitter_up = Entity(texture=menu_splitter, alpha = 0, model='quad', scale=(1.720, 0.120, 0), position=[0,0.4,0],parent=camera.ui)
        self.splitter_down = Entity(texture=menu_splitter, alpha = 0, model='quad', scale=(1.720, 0.120, 0), position=[0,-0.4,0],parent=camera.ui, rotation_z = 180)

        # A kattintható felületek a játék fülnél
        self.new_game_button = Entity(texture=new_game, alpha=0, scale=(0.6, 0.35, 0), position=[-2, 0.15, 0], model='quad', collider='box', parent=camera.ui, on_click=Func(new_game_pressed, self), on_mouse_enter=Func(new_game_hovered, self), on_mouse_exit=Func(new_game_exit, self))
        self.load_game_button = Entity(texture=load_game, alpha=0, scale=(0.6, 0.6, 0), position=[-2, 0, 0], model='quad', collider='box', parent=camera.ui, on_click=Func(load_game_pressed, self), on_mouse_enter=Func(load_game_hovered, self), on_mouse_exit=Func(load_game_exit, self))
        self.exit_game_button = Entity(texture=exit_game, alpha=0, scale=(0.6, 0.35, 0), position=[-2, -0.15, 0], model='quad', collider='box', parent=camera.ui, on_click=Func(exit_game_pressed, self), on_mouse_enter=Func(exit_game_hovered, self), on_mouse_exit=Func(exit_game_exit, self))

        # a játék fülnél a kattintható felületeket kijelölő piros keret
        self.new_game_hightlighted = Entity(texture = new_game_highlight, alpha = 0, model='quad', scale=(0.6, 0.35, 0), position=[0.42, 0.17, 0], parent=camera.ui)
        self.load_game_hightlighted = Entity(texture = load_game_highlight, alpha = 0, model='quad', scale=(0.6, 0.6, 0), position=[-0.2, 0, 0], parent=camera.ui)
        self.exit_game_hightlighted = Entity(texture = exit_game_highlight, alpha = 0, model='quad', scale=(0.6, 0.35, 0), position=[0.50, -0.15, 0], parent=camera.ui)

        # Játék fülnél a bal lenti magyarázó szöveg
        self.play_explaining_text = Text(text="", position=[-0.75, -0.44, 0], color = rgb(101, 101, 101), parent=camera.ui, font='fonts/pricedown.otf', scale = [1.4, 1.2, 0])
        self.play_explaining_text.fade_out(value=0.5, duration=0)

        # Címék a Játék fülnél -: Betöltés, Kilépés, Új játék
        self.new_game_text = Text(text="", position=[0.18, 0.11, 0], color = rgb(101, 101, 101), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.4, 1.2, 0])
        self.load_game_text = Text(text="", position=[-0.41, -0.16, 0], color=rgb(101, 101, 101), parent=camera.ui, font='fonts/TwCenMT.otf', scale=[1.4, 1.2, 0])
        self.exit_game_text = Text(text="", position=[0.33, -0.22, 0], color=rgb(101, 101, 101), parent=camera.ui, font='fonts/TwCenMT.otf', scale=[1.4, 1.2, 0])
        self.new_game_text.fade_out(value=0, duration=0)
        self.load_game_text.fade_out(value=0, duration=0)
        self.exit_game_text.fade_out(value=0, duration=0)

        # ESC lenyomva [Vissza]
        self.back_fromplay = Text(text="", position=[0.62, -0.43, 0], color=rgb(101, 101, 101),parent=camera.ui, font='fonts/TwCenMT.otf', scale=[1.3, 1.1, 0])
        self.click_area_back_fromplay = Entity(alpha=0, scale=(0.16, 0.05, 0), position=[0.69, -0.445, 0], model='quad',collider='box', parent=camera.ui, on_click=Func(back_pressed, self), on_mouse_enter=Func(menu_buttons_hovered, self.back_fromplay), on_mouse_exit=Func(menu_buttons_exit, self.back_fromplay))
        self.click_area_back_fromplay.disable()
        self.back_fromplay.fade_out(value=0, duration=0)

        ################################################################################################################
        # Init -> Loads

        pos_list = [[0.35,0.32],[0.35,0.28],[0.35,0.24],[0.35,0.2],[0.35,0.16],[0.35,0.12],[0.35,0.08],[0.35,0.04],[0.35,0],[0.35,-0.04],[0.35,-0.08],[0.35,-0.12],[0.35,-0.16],[0.35,-0.20],[0.35,-0.24],[0.35,-0.28],[0.35,-0.32]]

        for pos in pos_list:
            loadline = Loads(pos[0], pos[1], language_file)
            loads_list.append(loadline)

        show_outside_init() # kint van a class és a hozzá tartozó függvények felett.

        ################################################################################################################
        # QUIT Menu




    # [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

    def show_menu(self): # megjeleníti az alap menüt
        self.location = 'main'
        self.r.animate_position([-0.38, 0.35, 0], curve=curve.in_quart, duration=0.3, delay=0.80)
        self.e1.animate_position([-0.25, 0.35, 0], curve=curve.in_quart, duration=0.3, delay=0.75)
        self.d.animate_position([-0.13, 0.35, 0], curve=curve.in_quart, duration=0.3, delay=0.70)
        self.n.animate_position([0.01, 0.35, 0], curve=curve.in_quart, duration=0.3, delay=0.65)
        self.o.animate_position([0.15, 0.35, 0], curve=curve.in_quart, duration=0.3, delay=0.60)
        self.t.animate_position([0.28, 0.35, 0], curve=curve.in_quart, duration=0.3, delay=0.55)
        self.e2.animate_position([0.4, 0.35, 0], curve=curve.in_quart, duration=0.3, delay=0.50)
        self.background.fade_in(value=1, duration=0.2, delay = 0.5)

        self.click_area_play.enable()
        self.click_area_settings.enable()
        self.click_area_quit.enable()

        self.shadow.fade_in(value=1, duration=0.2, delay = 0.4)
        self.text_play.fade_in(value=1, duration=0.2, delay = 0.5)
        self.text_settings.fade_in(value=1, duration=0.2, delay = 0.5)
        self.text_quit.fade_in(value=1, duration=0.2, delay = 0.5)

    def hide_menu(self): # animálva elrejti az alap menüt.
        self.r.animate_position([-1, 0.35, 0], curve=curve.in_quart, duration=0.2, delay = 0.01)
        self.d.animate_position([-1, 0.35, 0], curve=curve.in_quart, duration=0.2, delay=0.06)
        self.n.animate_position([-1, 0.35, 0], curve=curve.in_quart, duration=0.2, delay=0.08)
        self.o.animate_position([-1, 0.35, 0], curve=curve.in_quart, duration=0.2, delay=0.1)
        self.t.animate_position([-1, 0.35, 0], curve=curve.in_quart, duration=0.2, delay=0.12)
        self.e2.animate_position([-2, 0.35, 0], curve=curve.in_quart, duration=0.25, delay=0.14)
        self.e1.animate_position([-2, 0.35, 0], curve=curve.in_quart, duration=0.25, delay=0.1)
        self.background.fade_out(value = 0, duration = 0.2)

        self.click_area_play.disable()
        self.click_area_settings.disable()
        self.click_area_quit.disable()

        self.text_play.color = rgb(101,101,101)
        self.text_settings.color = rgb(101, 101, 101)
        self.text_quit.color = rgb(101, 101, 101)

        self.shadow.fade_out(value = 0, duration = 0.2)
        self.text_play.fade_out(value = 0, duration = 0.2)
        self.text_settings.fade_out(value = 0, duration = 0.2)
        self.text_quit.fade_out(value = 0, duration = 0.2)

    # [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
    # [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

    def show_play_menu(self):
        if self.location != 'quit_main':
            self.new_game_button.fade_in(value = 1, duration = 0.5, delay = 0.35)
            self.load_game_button.fade_in(value = 1, duration = 0.6, delay = 0.40)
            self.exit_game_button.fade_in(value = 1, duration = 0.5, delay = 0.45)

            self.new_game_button.enable()
            self.load_game_button.enable()
            self.exit_game_button.enable()

            self.new_game_button.animate_position([0.42, 0.15, 0], curve=curve.in_sine, duration=0.4, delay=0.4)
            self.load_game_button.animate_position([-0.2, 0, 0], curve=curve.in_sine, duration=0.4, delay=0.4)
            self.exit_game_button.animate_position([0.50, -0.15, 0], curve=curve.in_sine, duration=0.4, delay=0.4)

            self.menu_title.text = self.language_file[0].get('GAMETITLE')
            self.menu_title.animate_position([-0.75, 0.46, 0], curve = curve.linear, duration = 0.12, delay = 0.5)
            self.new_game_text.text = self.language_file[0].get('NewGame')
            self.load_game_text.text = self.language_file[0].get('LoadGame')
            self.exit_game_text.text = self.language_file[0].get('QuitGame')
            self.new_game_text.fade_in(value=1, duration=0.4, delay = 0.7)
            self.load_game_text.fade_in(value=1, duration=0.4, delay = 0.75)
            self.exit_game_text.fade_in(value=1, duration=0.5, delay = 0.8)
            self.back_fromplay.fade_in(value=1, duration=0.5, delay = 0.5)
            self.play_explaining_text.text = ""
            self.play_explaining_text.fade_out(value=1, duration=0.4)

            self.new_game_button.collider = 'box'
            self.load_game_button.collider = 'box'
            self.exit_game_button.collider = 'box'

        self.location = 'play'

        self.splitter_up.fade_in(value=1, duration=0.7, delay=0.1)
        self.splitter_down.fade_in(value=1, duration=0.7, delay=0.1)
        self.click_area_back_fromplay.enable()
        self.back_fromplay.text = self.language_file[0].get('Back')

    def hide_play_menu(self):
        if self.location == 'play':
            self.splitter_up.fade_out(value=0, duration=0.7, delay=0.1)
            self.splitter_down.fade_out(value=0, duration=0.7, delay=0.1)
            self.menu_title.animate_position([-2, 0.46, 0], curve=curve.in_quart, duration=0.12, delay=0.5)

            self.back_fromplay.fade_out(value=0, duration=0.5, delay=0.5)
            self.click_area_back_fromplay.disable()
            self.back_fromplay.text = ""

        self.new_game_button.animate_position([-2, 0.15, 0], curve=curve.in_quart, duration=0.4, delay=0.2)
        self.load_game_button.animate_position([-2, 0, 0], curve=curve.in_quart, duration=0.4, delay=0.25)
        self.exit_game_button.animate_position([-2, -0.15, 0], curve=curve.in_quart, duration=0.4, delay=0.30)

        self.new_game_text.text = ""
        self.load_game_text.text = ""
        self.exit_game_text.text = ""
        self.new_game_text.fade_out(value=0, duration=0.4, delay=0.7)
        self.load_game_text.fade_out(value=0, duration=0.4, delay=0.75)
        self.exit_game_text.fade_out(value=0, duration=0.5, delay=0.8)
        self.play_explaining_text.fade_out(value=0, duration=0)

        self.load_game_hightlighted.fade_out(value=0, duration=0)
        self.new_game_hightlighted.fade_out(value=0, duration=0)
        self.exit_game_hightlighted.fade_out(value=0, duration=0)

        self.new_game_button.collider = None
        self.load_game_button.collider = None
        self.exit_game_button.collider = None

    ####################################################################################################################

    def delayed_show_load_menu(self):
        loadbar_counter = 0
        for loadbar in loads_list:
            if loadbar.file != None:
                loadbar.loadbar_text.text = self.savetitle[loadbar_counter].split('.')[0] # - a mentések itt kapnak címet
                loadbar_counter += 1

                loadbar.loadbar_text_date.text = f"{loadbar.file[3]}  -  {loadbar.file[2]}"
                loadbar.loadbar_text.fade_in(value=1, duration=0.5, delay=0.3)
                loadbar.loadbar_text_date.fade_in(value=1, duration=0.2, delay=0.08)
                loadbar.loadbar_text.color = rgb(125, 125, 125)
            else:
                loadbar.loadbar_text.color = rgb(60, 60, 60)
                loadbar.loadbar_text.text = "Empty Slot"

    def show_load_menu(self):
        self.savetitle = []
        loadfile_counter = 0
        for file_ in os.listdir('./saves'):
            if file_.endswith('.rsf'):
                save_file = fileread(f"saves/{file_}")
                loads_list[loadfile_counter].file = save_file
                self.savetitle.append(file_)

                loadfile_counter += 1
        print(self.savetitle)

        self.location = 'load'
        self.menu_title.text = self.language_file[0].get('LOADTITLE')
        #self.menu_title.animate_position([0.01, 0.46, 0], curve=curve.in_quart, duration=0.22, delay=0.1)
        self.menu_title.shake(duration=.25, magnitude=5, speed=.05, direction=(1,0.5))
        self.menu_title.appear(speed=.025, delay=0.15)

        for loadbar in loads_list:
            Loads.show_menubars(loadbar)

        invoke(Menu.delayed_show_load_menu, self, delay = 0.6)

    def hide_load_menu(self):
        global menu_loadbar_pressed
        for i in loads_list:
            Loads.hide_menubars(i)

        menu_loadbar_pressed = False

    #######################################################################################

    def show_exit_game(self):
        self.menu_title.text = self.language_file[0].get('QUITTITLE')
        self.menu_title.shake(duration=.25, magnitude=5, speed=.05, direction=(1, 0.5))
        self.menu_title.appear(speed=.025, delay=0.15)

    #######################################################################################

    def back(self):
        back_pressed(self)

def loadbar_click(self):
    global menu_loadbar_pressed, title_txt, date_txt, usrname_label, ingame_date_label, wealth_label, creation_date_label, playtime_label, \
        cheats_label, mission_description_label, username_txt, ingame_date_txt, wealth_txt, creation_date_txt, playtime_txt, cheats_txt, description_text

    if self.file != None:
        for i in loads_list:
            if i.file != None:
                i.loadbar_text.color = rgb(125, 125, 125)
            i.loadbar_selected.alpha = 0
        self.loadbar_selected.alpha = 1
        self.loadbar_text.color = rgb(236, 102, 108)

        if menu_loadbar_pressed == False:
            menu_loadbar_pressed = True
            infobg.animate_position([-0.55, 0, 0], curve=curve.linear, duration=0.4, delay=0.1)
            for objs in load_info_list:
                objs.fade_in(value = 0.5, duration = 0.4, delay = 0.3)

        # ------------------------------------------------------------------
        # Címkék

        title_txt.text = self.loadbar_text.text
        update_date = self.loadbar_text_date.text.split('-')[1].split('/')
        date_txt.text = f'{update_date[0]} / {update_date[1]} / {update_date[2]}          {self.loadbar_text_date.text.split("-")[0]}'

        usrname_label.text = self.language_file[0].get('Player')
        ingame_date_label.text = self.language_file[0].get('Season')
        wealth_label.text = self.language_file[0].get('Wealth')

        creation_date_label.text = self.language_file[0].get('Created')
        playtime_label.text = self.language_file[0].get('Playtime')
        cheats_label.text = self.language_file[0].get('Cheats')
        mission_description_label.text = self.language_file[0].get('Mission')

        # ------------------------------------------------------------------

        username_txt.text = self.file[9]
        ingame_date_txt.text = f'{self.language_file[0].get(self.file[11].split("*")[0])} {self.file[11].split("*")[1]}.'
        wealth_txt.text = self.file[12]

        creation_date_txt.text = self.file[14]
        playtime_txt.text = self.file[15]
        cheats_txt.text = self.language_file[0].get(self.file[17])

        print(self.file[17])

def loadbar_hovered(self):
    self.loadbar.texture = loadbar_active
def loadbar_leave(self):
    self.loadbar.texture = loadbar_deactive

class Loads():
    def __init__(self, x, y, language_file):
        self.language_file = language_file
        self.file = None
        self.x = x
        self.y = y

        self.loadbar = Entity(texture = loadbar_deactive, alpha=0, model='quad', scale=(1.02, 0.05, 0), position=[x, y, 0], parent=camera.ui)
        self.load_clickable = Entity(alpha=0, scale=(1.02, 0.038, 0), position=[x, y, 0], model='quad', collider='box', parent=camera.ui, on_click=Func(loadbar_click, self), on_mouse_enter=Func(loadbar_hovered, self), on_mouse_exit=Func(loadbar_leave, self))
        self.load_clickable.disable()

        self.loadbar_text = Text(text = "", position=[x - 0.49, y + 0.009,  -0.01], color = rgb(125, 125, 125), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1, 0.8, 0])
        self.loadbar_selected = Entity(texture = loadbar_selected, alpha=0, model='quad', scale=(1.02, 0.05, 0), position=[x, y, -0.01], parent=camera.ui)
        self.loadbar_text_date = Text(text="", position=[x + 0.29, y + 0.009,  -0.01], color=rgb(90, 90, 90),parent=camera.ui, font='fonts/TwCenMT.otf', scale=[0.8, 0.8, 0])

    def show_menubars(self):
        self.load_clickable.enable()
        self.loadbar.fade_in(value=1, duration=0.5, delay = 0.3)

    def hide_menubars(self):
        self.load_clickable.disable()
        if self.file != None:
            self.loadbar_text.color = rgb(125, 125, 125)
        self.loadbar.fade_in(value=0, duration=0.5, delay=0.1)
        self.loadbar.shake(duration=.6, magnitude=0.5, speed=.05, direction=(1, 0.5))
        self.loadbar_text.fade_in(value=0, duration=0.5, delay=0.1)
        self.loadbar_text_date.fade_in(value=0, duration=0.2, delay=0.3)
        self.loadbar_selected.fade_in(value=0, duration=0.5, delay=0.1)
        infobg.animate_position([-2, 0, 0], curve=curve.in_quart, duration=0.3, delay=0.2)

        for objs in load_info_list:
            objs.fade_in(value=0, duration=0.15, delay=0.05)

