
from PIL import Image
from ursina import *
from functions import fileread

# menu backgrounds
morning_bg1 = 'menu/main_menu/background/menu_morning_3.png'
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

def menu_play_pressed():
    print('klikk')
def menu_buttons_hovered(a):
    a.color = rgb(150, 150, 150)
def menu_buttons_exit(a):
    a.color = rgb(101, 101, 101)

class Menu(Entity):
    def __init__(self, language_file):

        self.language_file = language_file[0].split('*')
        self.pos_letters = [[-0.38, 0.35, 0],[-0.25, 0.35, 0],[-0.13, 0.35, 0],[0.01, 0.35, 0],[0.15, 0.35, 0],[0.28, 0.35, 0],[0.4, 0.35, 0]]
        self.verts = [(0, 0, 0), (2, 0, 0), (0, 1, 0), (0, 1, 0)]
        self.tris = [1, 2, 0, 2, 3, 0]
        #model = Mesh(vertices=self.verts, triangles=self.tris)

    def show_menu(self):
        self.canvas = Entity(color = color.black, model= 'quad', scale=(1.920, 1.080, 0), position = [0, 0, 0], parent = camera.ui)

        print(f'language file: {self.language_file}')

        self.background = Entity(texture = day_bg1, model='quad', scale=(1, 1, 0), position=[0, -0.0, 0], parent=self.canvas)
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

        self.click_area_play = Entity(alpha = 0, scale=(0.1, 0.05, 0), position = [0.782, -0.472, 0], model= 'quad', collider = 'box', parent = camera.ui, on_click = menu_play_pressed, on_mouse_enter = Func(menu_buttons_hovered, self.text_play), on_mouse_exit = Func(menu_buttons_exit, self.text_play))
        self.click_area_settings = Entity(alpha = 0, scale=(0.17, 0.05, 0), position = [0.57, -0.472, 0], model= 'quad', collider = 'box', parent = camera.ui, on_click = menu_play_pressed, on_mouse_enter = Func(menu_buttons_hovered, self.text_settings), on_mouse_exit = Func(menu_buttons_exit, self.text_settings))
        self.click_area_quit = Entity(alpha = 0, scale=(0.13, 0.05, 0), position = [0.325, -0.472, 0], model= 'quad', collider = 'box', parent = camera.ui, on_click = menu_play_pressed, on_mouse_enter = Func(menu_buttons_hovered, self.text_quit), on_mouse_exit = Func(menu_buttons_exit, self.text_quit))

    def hide_menu(self):
        pass
