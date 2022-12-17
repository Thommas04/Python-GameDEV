
# REDNOTE - HUD
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] #

from ursina import *

weapon_wheel = 'hud/weapon_wheel/weapon_wheel.png'
wheelbar_selected = 'hud/weapon_wheel/wheel_choosen.png'


class Hud(Entity):
    def main_weaponbar_click(self):
        print('click')
    def ww_r_click(self):
        print('click1')
    def ww_lr_click(self):
        print('click2')
    def ww_down_click(self):
        print('click3')
    def ww_ll_click(self):
        print('click4')
    def ww_l_click(self):
        print('click5')


    def main_weaponbar_hover(self):
        print('hover')
    def main_weaponbar_leave(self):
        print('leave')

    def ww_r_hover(self):
        print('hover1')
    def ww_r_leave(self):
        print('leave1')

    def ww_lr_hover(self):
        print('hover2')
    def ww_lr_leave(self):
        print('leave2')

    def ww_down_hover(self):
        print('hover3')
    def ww_down_leave(self):
        print('leave3')

    def ww_ll_hover(self):
        print('hover4')
    def ww_ll_leave(self):
        print('leave4')

    def ww_l_hover(self):
        print('hover5')
    def ww_l_leave(self):
        print('leave5')

    def __init__(self, language_file, pause_menu):

        verts1 = [(0.237, 0.07, 0), (0.925, 0.478, 0), (0.392, 0.65, 0), (-0.397, 0.647, 0), (-1.058, 0.414, 0), (-0.244, 0.07, 0), (-0.181, 0.151, 0), (-0.092, 0.205, 0), (0.018, 0.226, 0), (0.175, 0.172, 0)]
        tris1 = [0,1,9,9,1,2,9,2,3,9,3,8,8,3,7,7,3,4,7,4,6,6,4,5]
        verts2 = [(0.244, 0.075, 0), (0.963, 0.485, 0), (1.103, 0.34, 0), (1.11, -0.35, 0), (0.244, -0.133, 0), (0.268, -0.039, 0)]
        tris2 = [0,1,2,0,2,5,2,5,3,5,4,3]
        verts3 = [(0.249, -0.134, 0), (1.156, -0.377, 0), (1.106, -0.649, 0), (0.282, -0.647, 0), (0.11, -0.263, 0), (0.193, -0.202, 0)]
        tris3 = [0, 1, 2, 0, 2, 5, 2, 5, 3, 5, 4, 3]
        verts4 = [(0.107, -0.267, 0), (0.278, -0.65, 0), (-0.241, -0.649, 0), (-0.092, -0.269, 0), (0.009, -0.288, 0)]
        tris4 = [0,1,4,4,1,2,3,4,2]
        verts5 = [(-0.091, -0.27, 0), (-0.222, -0.647, 0), (-0.998, -0.647, 0), (-1.156, -0.466, 0), (-0.231, -0.134, 0), (-0.172, -0.214, 0)]
        tris5 = [0,1,2,0,2,5,5,2,3,5,3,4]
        verts6 = [(-0.231, -0.137, 0), (-1.159, -0.528, 0), (-1.156, 0.441, 0), (-0.241, 0.065, 0), (-0.258, -0.032, 0)]
        tris6 = [0,1,2,0,2,4,4,2,3]

        self.main_weaponbar = Entity(collider='mesh', model=Mesh(vertices=verts1, triangles=tris1, thickness=4),position = (0,-0.01,0), scale = (0.8,0.8,0.4), alpha = 0, z=-1, parent = camera.ui, on_click = Func(Hud.main_weaponbar_click, self), on_mouse_enter = Func(Hud.main_weaponbar_hover, self) , on_mouse_exit = Func(Hud.main_weaponbar_leave, self) )
        self.weapon_wheel_right = Entity(collider='mesh', model=Mesh(vertices=verts2, triangles=tris2, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, z=-1, parent=camera.ui, on_click=Func(Hud.ww_r_click, self), on_mouse_enter=Func(Hud.ww_r_hover, self), on_mouse_exit=Func(Hud.ww_r_leave, self))
        self.weapon_wheel_lowerright = Entity(collider='mesh', model=Mesh(vertices=verts3, triangles=tris3, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, z=-1, parent=camera.ui, on_click=Func(Hud.ww_lr_click, self), on_mouse_enter=Func(Hud.ww_lr_hover, self), on_mouse_exit=Func(Hud.ww_lr_leave, self))
        self.weapon_wheel_down = Entity(collider='mesh', model=Mesh(vertices=verts4, triangles=tris4, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, z=-1, parent=camera.ui, on_click=Func(Hud.ww_down_click, self), on_mouse_enter=Func(Hud.ww_down_hover, self), on_mouse_exit=Func(Hud.ww_down_leave, self))
        self.weapon_wheel_lowerleft = Entity(collider='mesh', model=Mesh(vertices=verts5, triangles=tris5, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, z=-1, parent=camera.ui, on_click=Func(Hud.ww_ll_click, self), on_mouse_enter=Func(Hud.ww_ll_hover, self), on_mouse_exit=Func(Hud.ww_ll_leave, self))
        self.weapon_wheel_left = Entity(collider='mesh', model=Mesh(vertices=verts6, triangles=tris6, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, z=-1, parent=camera.ui, on_click=Func(Hud.ww_l_click, self), on_mouse_enter=Func(Hud.ww_l_hover, self), on_mouse_exit=Func(Hud.ww_l_leave, self))

        self.weapon_wheel_list = [self.main_weaponbar, self.weapon_wheel_right, self.weapon_wheel_lowerright, self.weapon_wheel_down, self. weapon_wheel_lowerleft, self. weapon_wheel_left]
        for i in self.weapon_wheel_list:
            i.disable()

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

