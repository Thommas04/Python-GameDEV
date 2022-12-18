
# REDNOTE - HUD
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] #

from ursina import *

weapon_wheel = 'hud/weapon_wheel/weapon_wheel.png'
wheelbar_selected = 'hud/weapon_wheel/wheel_choosen.png'

# [ Vertices and Triangles ] ------------------------------------------------------------------------------------------[]

# Upper side of weapon wheel (3)
verts00 = [(-0.101, 0.193, 0), (-0.442, 0.65, 0), (0.404, 0.652, 0), (0.095, 0.208, 0), (0.0, 0.226, 0)]
tris00 = [0, 1, 4, 4, 1, 2, 4, 3, 2]
verts01 = [(-0.104, 0.196, 0), (-0.445, 0.65, 0), (-1.159, 0.652, 0), (-1.156, 0.377, 0), (-0.237, 0.069, 0), (-0.183, 0.146, 0)]
tris01 = [4, 5, 3, 5, 3, 2, 5, 2, 1, 5, 0, 1]
verts02 = [(0.098, 0.205, 0), (0.406, 0.652, 0), (1.061, 0.652, 0), (1.153, 0.583, 0), (0.237, 0.066, 0), (0.186, 0.148, 0)]
tris02 = [0, 1, 5, 5, 1, 2, 5, 2, 3, 3, 5, 4]

# weapon wheel : right, lower_right, down, lower_left, left
verts2 = [(0.244, 0.075, 0), (0.963, 0.485, 0), (1.103, 0.34, 0), (1.11, -0.35, 0), (0.244, -0.133, 0), (0.268, -0.039, 0)]
tris2 = [0, 1, 2, 0, 2, 5, 2, 5, 3, 5, 4, 3]
verts3 = [(0.249, -0.134, 0), (1.156, -0.377, 0), (1.106, -0.649, 0), (0.282, -0.647, 0), (0.11, -0.263, 0), (0.193, -0.202, 0)]
tris3 = [0, 1, 2, 0, 2, 5, 2, 5, 3, 5, 4, 3]
verts4 = [(0.107, -0.267, 0), (0.278, -0.65, 0), (-0.241, -0.649, 0), (-0.092, -0.269, 0), (0.009, -0.288, 0)]
tris4 = [0, 1, 4, 4, 1, 2, 3, 4, 2]
verts5 = [(-0.091, -0.27, 0), (-0.222, -0.647, 0), (-0.998, -0.647, 0), (-1.156, -0.466, 0), (-0.231, -0.134, 0), (-0.172, -0.214, 0)]
tris5 = [0, 1, 2, 0, 2, 5, 5, 2, 3, 5, 3, 4]
verts6 = [(-0.231, -0.137, 0), (-1.159, -0.528, 0), (-1.156, 0.441, 0), (-0.241, 0.065, 0), (-0.258, -0.032, 0)]
tris6 = [0, 1, 2, 0, 2, 4, 4, 2, 3]

# [ HUD CLASS ] -------------------------------------------------------------------------------------------------------[]

class WeaponWheel(Entity):
    def weaponbars_click(self, type):
        if type == 'super':
            print('main c')
        if type == 'upper_left':
            print('upper_left_click')
        if type == 'upper_right':
            print('upper_right_click')

        if type == 'right':
            print('r c')
        if type == 'lower_right':
            print('lr c')
        if type == 'down':
            print('d c')
        if type == 'lower_left':
            print('ll c')
        if type == 'left':
            print('l c')

    def weaponbars_hover(self, type):
        if type == 'super':
            self.wheelbar_selector.rotation = (0, 0, 90)
            self.wheelbar_selector.scale = (0.2, 0.3, 0)
            self.wheelbar_selector.position = (0, 0.29, -0.1)
        if type == 'upper_left':
            self.wheelbar_selector.rotation = (0, 0, 48)
            self.wheelbar_selector.scale = (0.2, 0.3, 0)
            self.wheelbar_selector.position = (-0.215, 0.2, -0.1)
        if type == 'upper_right':
            self.wheelbar_selector.rotation = (0, 0, -47)
            self.wheelbar_selector.scale = (-0.2, -0.3, 0)
            self.wheelbar_selector.position = (0.215, 0.215, -0.1)


        if type == 'right':
            self.wheelbar_selector.rotation = (0, 0, 0)
            self.wheelbar_selector.scale = (-0.2, -0.3, 0)
            self.wheelbar_selector.position = (0.32, -0.02, -0.1)
        if type == 'lower_right':
            self.wheelbar_selector.rotation = (0, 0, 45)
            self.wheelbar_selector.scale = (-0.2, -0.3, 0)
            self.wheelbar_selector.position = (0.237, -0.25, -0.1)
        if type == 'down':
            self.wheelbar_selector.rotation = (0, 0, 90)
            self.wheelbar_selector.scale = (-0.2, -0.3, 0)
            self.wheelbar_selector.position = (0.014, -0.346, -0.1)
        if type == 'lower_left':
            self.wheelbar_selector.rotation = (0, 0, -45)
            self.wheelbar_selector.scale = (0.2, 0.3, 0)
            self.wheelbar_selector.position = (-0.215, -0.26, -0.1)
        if type == 'left':
            self.wheelbar_selector.rotation = (0,0,0)
            self.wheelbar_selector.scale = (0.2, 0.3, 0)
            self.wheelbar_selector.position = (-0.32, -0.035, -0.1)

        self.wheelbar_selector.fade_in(value=1, duration=0.15, delay = 0)

    def weaponbars_leave(self, type):
        if type == 'super':
            print('main leave')
        if type == 'upper_left':
            pass
        if type == 'upper_right':
            print('leaveeeee')

        if type == 'right':
            print('r leave')
        if type == 'lower_right':
            print('lr leave')
        if type == 'down':
            print('d leave')
        if type == 'lower_left':
            print('ll leave')
        if type == 'left':
            print('l leave')



    def __init__(self, language_file, pause_menu):
        self.weapon_wheel_super = Entity(collider='mesh', model=Mesh(vertices=verts00, triangles=tris00, thickness=4), position = (0,-0.01,0), scale = (0.8,0.8,0.4), alpha = 0, parent = camera.ui, on_click = Func(WeaponWheel.weaponbars_click, self, 'super'), on_mouse_enter = Func(WeaponWheel.weaponbars_hover, self, 'super'), on_mouse_exit = Func(WeaponWheel.weaponbars_leave, self, 'super'))
        self.weapon_wheel_upperleft = Entity(collider='mesh', model=Mesh(vertices=verts01, triangles=tris01, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_click=Func(WeaponWheel.weaponbars_click, self, 'upper_left'), on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'upper_left'), on_mouse_exit=Func(WeaponWheel.weaponbars_leave, self, 'upper_left'))
        self.weapon_wheel_upperright = Entity(collider='mesh', model=Mesh(vertices=verts02, triangles=tris02, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_click=Func(WeaponWheel.weaponbars_click, self, 'upper_right'), on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'upper_right'), on_mouse_exit=Func(WeaponWheel.weaponbars_leave, self, 'upper_right'))

        self.weapon_wheel_right = Entity(collider='mesh', model=Mesh(vertices=verts2, triangles=tris2, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_click=Func(WeaponWheel.weaponbars_click, self, 'right'), on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'right'), on_mouse_exit=Func(WeaponWheel.weaponbars_leave, self, 'right'))
        self.weapon_wheel_lowerright = Entity(collider='mesh', model=Mesh(vertices=verts3, triangles=tris3, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_click=Func(WeaponWheel.weaponbars_click, self, 'lower_right'), on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'lower_right'), on_mouse_exit=Func(WeaponWheel.weaponbars_leave, self, 'lower_right'))
        self.weapon_wheel_down = Entity(collider='mesh', model=Mesh(vertices=verts4, triangles=tris4, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_click=Func(WeaponWheel.weaponbars_click, self, 'down'), on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'down'), on_mouse_exit=Func(WeaponWheel.weaponbars_leave, self, 'down'))
        self.weapon_wheel_lowerleft = Entity(collider='mesh', model=Mesh(vertices=verts5, triangles=tris5, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_click=Func(WeaponWheel.weaponbars_click, self, 'lower_left'), on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'lower_left'), on_mouse_exit=Func(WeaponWheel.weaponbars_leave, self, 'lower_left'))
        self.weapon_wheel_left = Entity(collider='mesh', model=Mesh(vertices=verts6, triangles=tris6, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_click=Func(WeaponWheel.weaponbars_click, self, 'left'), on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'left'), on_mouse_exit=Func(WeaponWheel.weaponbars_leave, self, 'left'))

        self.weapon_wheel_list = [self.weapon_wheel_super, self.weapon_wheel_upperleft, self.weapon_wheel_upperright, self.weapon_wheel_right, self.weapon_wheel_lowerright, self.weapon_wheel_down, self. weapon_wheel_lowerleft, self. weapon_wheel_left]
        for i in self.weapon_wheel_list:
            i.disable()

        self.wheelbar_selector = Entity(texture = wheelbar_selected, model = 'quad', position = (0, 0, -0.1), scale = (0.2, 0.3, 0), alpha = 0, parent = camera.ui)

        self.language_file = language_file
        self.pause_menu = pause_menu
        self.wheel = Entity(texture=weapon_wheel, alpha = 0, model='quad', scale=(0.8, 0.8, 0), position=[0,-0.02,0],parent=camera.ui)

    def show_weaponwheel(self):
        self.wheel.fade_in(value=1, duration=0.15, delay = 0)
        self.pause_menu.filters.setBlurSharpen(amount=0)
        for i in self.weapon_wheel_list:
            i.enable()

    def hide_weaponwheel(self):
        self.wheel.fade_in(value=0, duration=0.15, delay = 0)
        self.pause_menu.filters.setBlurSharpen(amount=1)
        for i in self.weapon_wheel_list:
            i.disable()

