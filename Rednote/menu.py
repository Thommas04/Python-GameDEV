
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

# menu buttons
new_game = 'menu/main_menu/buttons/new_game.png'
load_game = 'menu/main_menu/buttons/load_game.png'
exit_game = 'menu/main_menu/buttons/exit_game.png'
new_game_highlight = 'menu/main_menu/buttons/new_game_highlight.png'
load_game_highlight = 'menu/main_menu/buttons/load_game_highlight.png'
exit_game_highlight = 'menu/main_menu/buttons/exit_game_highlight.png'

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

def menu_play_pressed(a):
    Menu.show_play_menu(a)
    Menu.hide_menu(a)

def menu_settings_pressed(a):
    pass
def menu_quit_pressed(a):
    pass

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

def load_game_pressed(a):
    Menu.show_load_menu(a)
    Menu.hide_play_menu(a)

def new_game_pressed(a):
    pass

def exit_game_pressed(a):
    pass

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

#ESC lenyomva - Vissza
def back_pressed(a):
    if a.location == 'play':
        Menu.hide_play_menu(a)
        Menu.show_menu(a)
    if a.location == 'load':
        Menu.hide_load_menu(a)
        Menu.show_play_menu(a)
        a.menu_title.shake(duration=.25, magnitude=5, speed=.05, direction=(1, 0.5))
        a.menu_title.appear(speed=.025, delay=0.15)

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

def menu_buttons_hovered(a):
    a.color = rgb(150, 150, 150)
def menu_buttons_exit(a):
    a.color = rgb(101, 101, 101)

######################################

def load_game_hovered(self):
    self.load_game_hightlighted.fade_in(value = 1, duration = 0)
    self.play_explaining_text.text = self.language_file[3]
    self.load_game_text.color = rgb(236, 102, 108)
def load_game_exit(self):
    self.load_game_hightlighted.fade_out(value = 0, duration = 0)
    self.load_game_text.color = rgb(101, 101, 101)

def new_game_hovered(self):
    self.new_game_hightlighted.fade_in(value = 1, duration = 0)
    self.play_explaining_text.text = self.language_file[4]
    self.new_game_text.color = rgb(236, 102, 108)
def new_game_exit(self):
    self.new_game_hightlighted.fade_out(value = 0, duration = 0)
    self.new_game_text.color = rgb(101, 101, 101)

def exit_game_hovered(self):
    self.exit_game_hightlighted.fade_in(value = 1, duration = 0)
    self.play_explaining_text.text = self.language_file[5]
    self.exit_game_text.color = rgb(236, 102, 108)
def exit_game_exit(self):
    self.exit_game_hightlighted.fade_out(value = 0, duration = 0)
    self.exit_game_text.color = rgb(101,101,101)

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

class Menu(Entity):
    def __init__(self, language_file):

        self.location = 'main'
        self.language_file = language_file[0].split('*')
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
        self.menu_title = Text(text="", position=[-1, 0.46, 0], color=rgb(126, 126, 101), parent=camera.ui,font='fonts/pricedown.otf', scale=[1.7, 1.5, 0])

        # MAIN MENU # -------------------------------------------------------------------------------------------------

        self.shadow = Entity(texture=right_down_shadow, model='quad', scale=(1, 0.1, 0), position=[0.4,-0.45,0], parent=camera.ui)

        self.r = Entity(texture=letter_r, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[0],parent=camera.ui)
        self.e1 =Entity(texture=letter_e, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[1],parent=camera.ui)
        self.d = Entity(texture=letter_d, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[2],parent=camera.ui)
        self.n = Entity(texture=letter_n, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[3],parent=camera.ui)
        self.o = Entity(texture=letter_o, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[4],parent=camera.ui)
        self.t = Entity(texture=letter_t, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[5],parent=camera.ui)
        self.e2 =Entity(texture=letter_e, model='quad', scale=(0.18, 0.25, 0), position=self.pos_letters[6],parent=camera.ui)

        self.text_play = Text(text=self.language_file[0], position=[0.75, -0.456, 0], color = rgb(101, 101, 101), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.3, 1.1, 0])
        self.text_settings = Text(text=self.language_file[1], position=[0.5, -0.456, 0], color = rgb(101, 101, 101), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.3, 1.1, 0])
        self.text_quit = Text(text=self.language_file[2], position=[0.28, -0.456, 0], color = rgb(101, 101, 101), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1.3, 1.1, 0])

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
        self.exit_game_button = Entity(texture=exit_game, alpha=0, scale=(0.6, 0.35, 0), position=[-2, -0.15, 0], model='quad', collider='box', parent=camera.ui, on_click=Func(new_game_pressed, self), on_mouse_enter=Func(exit_game_hovered, self), on_mouse_exit=Func(exit_game_exit, self))

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

        self.loads_list = []
        for pos in pos_list:
            loadline = Loads(pos[0], pos[1])
            self.loads_list.append(loadline)

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

        self.shadow.fade_out(value = 0, duration = 0.2)
        self.text_play.fade_out(value = 0, duration = 0.2)
        self.text_settings.fade_out(value = 0, duration = 0.2)
        self.text_quit.fade_out(value = 0, duration = 0.2)

    # [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
    # [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

    def show_play_menu(self):
        self.location = 'play'
        self.splitter_up.fade_in(value = 1, duration = 0.7, delay = 0.1)
        self.splitter_down.fade_in(value = 1, duration = 0.7, delay = 0.1)

        self.new_game_button.fade_in(value = 1, duration = 0.5, delay = 0.35)
        self.load_game_button.fade_in(value = 1, duration = 0.6, delay = 0.40)
        self.exit_game_button.fade_in(value = 1, duration = 0.5, delay = 0.45)

        self.new_game_button.enable()
        self.load_game_button.enable()
        self.exit_game_button.enable()
        self.click_area_back_fromplay.enable()

        self.new_game_button.animate_position([0.42, 0.15, 0], curve=curve.in_sine, duration=0.4, delay=0.4)
        self.load_game_button.animate_position([-0.2, 0, 0], curve=curve.in_sine, duration=0.4, delay=0.4)
        self.exit_game_button.animate_position([0.50, -0.15, 0], curve=curve.in_sine, duration=0.4, delay=0.4)

        self.menu_title.text = self.language_file[6]
        self.menu_title.animate_position([-0.75, 0.46, 0], curve = curve.linear, duration = 0.12, delay = 0.5)
        self.back_fromplay.text = self.language_file[7]
        self.new_game_text.text = self.language_file[8]
        self.load_game_text.text = self.language_file[9]
        self.exit_game_text.text = self.language_file[10]
        self.new_game_text.fade_in(value=1, duration=0.4, delay = 0.7)
        self.load_game_text.fade_in(value=1, duration=0.4, delay = 0.75)
        self.exit_game_text.fade_in(value=1, duration=0.5, delay = 0.8)
        self.back_fromplay.fade_in(value=1, duration=0.5, delay = 0.5)
        self.play_explaining_text.text = ""
        self.play_explaining_text.fade_out(value=1, duration=0.4)

        self.new_game_button.collider = 'box'
        self.load_game_button.collider = 'box'
        self.exit_game_button.collider = 'box'

    def hide_play_menu(self):
        if self.location == 'play':
            self.splitter_up.fade_out(value=0, duration=0.7, delay=0.1)
            self.splitter_down.fade_out(value=0, duration=0.7, delay=0.1)
            self.menu_title.animate_position([-1, 0.46, 0], curve=curve.in_quart, duration=0.12, delay=0.5)

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

    def show_load_menu(self):

        for file in os.listdir('./saves'):
            if file.endswith('.rsf'):
                save_file = fileread(f"saves/{file}")
                self.loads_list[int(save_file[0])].file = save_file

        self.location = 'load'
        self.menu_title.text = 'JÁTÉK BETÖLTÉSE'
        #self.menu_title.animate_position([0.01, 0.46, 0], curve=curve.in_quart, duration=0.22, delay=0.1)
        self.menu_title.shake(duration=.25, magnitude=5, speed=.05, direction=(1,0.5))
        self.menu_title.appear(speed=.025, delay=0.15)

        for loadbar in self.loads_list:
            Loads.show_menubars(loadbar)
            if loadbar.file != None:
                loadbar.loadbar_text.text = loadbar.file[9]
                loadbar.loadbar_text.color = rgb(125, 125, 125)
            else:
                loadbar.loadbar_text.color = rgb(60, 60, 60)
                loadbar.loadbar_text.text = "Empty Slot"

    def hide_load_menu(self):
        for i in self.loads_list:
            Loads.hide_menubars(i)

    def back(self):
        back_pressed(self)

def loadbar_click(self):
    pass
def loadbar_hovered(self):
    self.loadbar.texture = loadbar_active
def loadbar_leave(self):
    self.loadbar.texture = loadbar_deactive

class Loads():
    def __init__(self, x, y):
        self.file = None
        self.x = x
        self.y = y

        self.load_clickable = Entity(alpha=0, scale=(1.02, 0.038, 0), position=[x, y, 0], model='quad', collider='box', parent=camera.ui, on_click=Func(loadbar_click, self), on_mouse_enter=Func(loadbar_hovered, self), on_mouse_exit=Func(loadbar_leave, self))
        self.load_clickable.disable()
        self.loadbar = Entity(texture = loadbar_deactive, alpha=0, model='quad', scale=(1.02, 0.05, 0), position=[x, y, 0], parent=camera.ui)

        self.loadbar_text = Text(text = "", position=[x - 0.49, y + 0.0074, 0], color = rgb(125, 125, 125), parent=camera.ui, font='fonts/TwCenMT.otf', scale = [1, 0.8, 0])

    def show_menubars(self):
        self.load_clickable.enable()
        self.loadbar.fade_in(value=1, duration=0.5, delay = 0.3)

    def hide_menubars(self):
        self.load_clickable.disable()
        self.loadbar.fade_in(value=0, duration=0.5, delay=0.1)
        self.loadbar.shake(duration=.6, magnitude=0.5, speed=.05, direction=(1, 0.5))

