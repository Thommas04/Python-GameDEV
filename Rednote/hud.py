
# REDNOTE - HUD
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] #

from ursina import *

# WEAPON WHEEL # ---------------------------------------------------*

weapon_wheel = 'hud/weapon_wheel/weapon_wheel.png'
wheelbar_selected = 'hud/weapon_wheel/wheel_choosen.png'

# ICONS

spencer_carbine_icon = 'hud/weapon_wheel_items/rifle_icon.png'
hand_icon = 'hud/weapon_wheel_items/hand_icon.png'
colt_icon = 'hud/weapon_wheel_items/revolver_icon.png'

# DEAD SCREEN # ------------------------------------------------------------*

dead_screen_spritesheet = 'hud/death_screen/death_screen_sheet.png'


# HUD # ------------------------------------------------------------*

minimap = 'hud/hud_widgets/minimap/minimap_frame.png'
core_frame_spritesheet = 'hud/hud_widgets/cores/core_frame_sheet.png'
core_spritesheet = 'hud/hud_widgets/cores/core_sheet.png'
core_bg_spritesheet = 'hud/hud_widgets/cores/core_bg_sheet.png'

# INVENTORY # ------------------------------------------------------------*

inventory_background = 'hud/inventory/widgets/inventory_bg.png'
inventory_buttons_spritesheet = 'hud/inventory/widgets/inventory_buttons_sheet.png'
inventory_selected_tile = 'hud/inventory/widgets/inventory_selected_tile.png'


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

# WEAPON WHEEL #

class WeaponWheel(Entity):
    def weaponbars_hover(self, type):
        if type == 'up':
            self.wheelbar_selector.rotation = (0, 0, 90)
            self.wheelbar_selector.scale = (0.2, 0.3, 0)
            self.wheelbar_selector.position = (0, 0.29, -0.1)
            self.selected_tile = type
        if type == 'upper_left':
            self.wheelbar_selector.rotation = (0, 0, 48)
            self.wheelbar_selector.scale = (0.2, 0.3, 0)
            self.wheelbar_selector.position = (-0.215, 0.2, -0.1)
            self.selected_tile = type
        if type == 'upper_right':
            self.wheelbar_selector.rotation = (0, 0, -47)
            self.wheelbar_selector.scale = (-0.2, -0.3, 0)
            self.wheelbar_selector.position = (0.215, 0.215, -0.1)
            self.selected_tile = type

        if type == 'right':
            self.wheelbar_selector.rotation = (0, 0, 0)
            self.wheelbar_selector.scale = (-0.2, -0.3, 0)
            self.wheelbar_selector.position = (0.32, -0.02, -0.1)
            self.selected_tile = type
        if type == 'lower_right':
            self.wheelbar_selector.rotation = (0, 0, 45)
            self.wheelbar_selector.scale = (-0.2, -0.3, 0)
            self.wheelbar_selector.position = (0.237, -0.25, -0.1)
            self.selected_tile = type
        if type == 'down':
            self.wheelbar_selector.rotation = (0, 0, 90)
            self.wheelbar_selector.scale = (-0.2, -0.3, 0)
            self.wheelbar_selector.position = (0.014, -0.346, -0.1)
            self.selected_tile = type
        if type == 'lower_left':
            self.wheelbar_selector.rotation = (0, 0, -45)
            self.wheelbar_selector.scale = (0.2, 0.3, 0)
            self.wheelbar_selector.position = (-0.215, -0.26, -0.1)
            self.selected_tile = type
        if type == 'left':
            self.wheelbar_selector.rotation = (0,0,0)
            self.wheelbar_selector.scale = (0.2, 0.3, 0)
            self.wheelbar_selector.position = (-0.32, -0.035, -0.1)
            self.selected_tile = type

        self.wheelbar_selector.fade_in(value=1, duration=0.15, delay = 0)

    def __init__(self, language_file, pause_menu):
        self.weapon_wheel_super = Entity(collider='mesh', model=Mesh(vertices=verts00, triangles=tris00, thickness=4), position = (0,-0.01,0), scale = (0.8,0.8,0.4), alpha = 0, parent = camera.ui, on_mouse_enter = Func(WeaponWheel.weaponbars_hover, self, 'up'))
        self.weapon_wheel_upperleft = Entity(collider='mesh', model=Mesh(vertices=verts01, triangles=tris01, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'upper_left'))
        self.weapon_wheel_upperright = Entity(collider='mesh', model=Mesh(vertices=verts02, triangles=tris02, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'upper_right'))

        self.weapon_wheel_right = Entity(collider='mesh', model=Mesh(vertices=verts2, triangles=tris2, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'right'))
        self.weapon_wheel_lowerright = Entity(collider='mesh', model=Mesh(vertices=verts3, triangles=tris3, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'lower_right'))
        self.weapon_wheel_down = Entity(collider='mesh', model=Mesh(vertices=verts4, triangles=tris4, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'down'))
        self.weapon_wheel_lowerleft = Entity(collider='mesh', model=Mesh(vertices=verts5, triangles=tris5, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'lower_left'))
        self.weapon_wheel_left = Entity(collider='mesh', model=Mesh(vertices=verts6, triangles=tris6, thickness=4), position=(0, -0.01, 0), scale=(0.8, 0.8, 0.4), alpha=0, parent=camera.ui, on_mouse_enter=Func(WeaponWheel.weaponbars_hover, self, 'left'))

        self.weapon_wheel_list = [self.weapon_wheel_super, self.weapon_wheel_upperleft, self.weapon_wheel_upperright, self.weapon_wheel_right, self.weapon_wheel_lowerright, self.weapon_wheel_down, self. weapon_wheel_lowerleft, self. weapon_wheel_left]
        for i in self.weapon_wheel_list:
            i.disable()

        self.wheelbar_selector = Entity(texture = wheelbar_selected, model = 'quad', position = (0, 0, -0.1), scale = (0.2, 0.3, 0), alpha = 0, parent = camera.ui)

        self.language_file = language_file
        self.pause_menu = pause_menu
        self.wheel = Entity(texture=weapon_wheel, alpha = 0, model='quad', scale=(0.8, 0.8, 0), position=[0,-0.02,0],parent=camera.ui)
        self.selected_tile = 'right'

        # -----------------------------------------------------
        # Icons

        self.up_icon = Entity(tag = '', texture = hand_icon, model = 'quad', position = (0, 0.245, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)
        self.upper_left_icon = Entity(tag = 'colt', rotation = (0,0,-40), texture = colt_icon, model = 'quad', position = (-0.162, 0.175, -0.1), scale = (0.165, 0.165, 0), alpha = 0, parent=camera.ui)
        self.upper_right_icon = Entity(tag = '', texture = hand_icon, model = 'quad', position = (0.2, 0.15, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)

        self.right_icon = Entity(tag = 'hand', texture = hand_icon, model = 'quad', position = (0.275, -0.022, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)
        self.left_icon = Entity(tag = '', texture = hand_icon, model = 'quad', position = (-0.26, -0.03, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)
        self.lower_left_icon = Entity(tag = '', texture = hand_icon, model = 'quad', position = (-0.17, -0.22, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)
        self.lower_right_icon = Entity(tag = '', texture = hand_icon, model = 'quad', position = (0.2, -0.21, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)
        self.down_icon = Entity(tag = '', texture = hand_icon, model = 'quad', position = (0.02, -0.295, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)


        self.wheel_icons_list = [self.right_icon, self.up_icon, self.upper_left_icon, self.upper_right_icon, self.left_icon, self.lower_left_icon, self.lower_right_icon, self.down_icon]

    def get_back_selected_wheeltile(self):
        return self.selected_tile


    def show_weaponwheel(self):
        self.wheel.fade_in(value=0.85, duration=0.15, delay = 0)
        self.pause_menu.filters.setBlurSharpen(amount=0)
        for i in self.weapon_wheel_list:
            i.enable()
        for icon in self.wheel_icons_list:
            icon.fade_in(value=0.8, duration=0.15, delay = 0)

    def hide_weaponwheel(self):
        self.wheel.fade_in(value=0, duration=0.15, delay = 0)
        self.pause_menu.filters.setBlurSharpen(amount=1)
        for i in self.weapon_wheel_list:
            i.disable()
        for icon in self.wheel_icons_list:
            icon.fade_in(value=0, duration=0.15, delay = 0)

########################################################################################################################
# HUD / CORES & Minimap #


class HUD(Entity):

    def delayed_static_show(self):
        self.dead_screen_anim.play_animation('static_show')

    def delayed_hide_deadscreen_bg(self):
        # EZ TÖRTÉNIK HA A PLAYER MEGHAL, MAJD ÚJRAÉLED
        # Statisztika mutató, rakja őt a kocsmába, ilyesmi

        self.dead_screen_anim.alpha = 0
        self.dead_screen_anim.play_animation('static_hide')
        self.dead_screen_bg.fade_in(value=0, duration=1)
        HUD.show_hud(self)

        self.dead_screen_status = 'respawned'

    def play_hide_deadscreen_anim(self):
        self.dead_screen_anim.play_animation('hide_dead_screen')
        invoke(HUD.delayed_hide_deadscreen_bg, self, delay=1)

    def play_deadscreen_anim(self):
        self.dead_screen_anim.alpha = 1
        self.dead_screen_anim.play_animation('show_dead_screen')
        invoke(HUD.delayed_static_show, self, delay=0.9)
        self.dead_continue_text.text = self.language_file[2].get('Continue')
        self.dead_continue_text.animate_color(rgb(101, 101, 101), duration = 1, delay = 1)
        self.dead_continue_click.enable()

    def show_death_screen(self):
        self.dead_screen_bg.fade_in(value = 1, duration = 1.5, delay = 1)

        invoke(HUD.play_deadscreen_anim,self, delay = 3)
        HUD.hide_hud(self, 1.5)

    def hide_death_screen(self):
        self.dead_continue_text.text = ''
        self.dead_continue_text.color = color.black
        self.dead_continue_click.disable()
        invoke(HUD.play_hide_deadscreen_anim, self, delay=2)


    def dead_continue_hover(self):
        self.dead_continue_text.color = rgb(125, 125, 125)
    def dead_continue_leave(self):
        self.dead_continue_text.color = rgb(101, 101, 101)

    # ------------------------------------------------------------------------------------------------------------------

    def anim_cores(self, player_stats):

        # -> health_core <-

        health_stat = player_stats.get('health')
        energy_stat = player_stats.get('energy')
        power_stat  = player_stats.get('power')
        hunger_stat = player_stats.get('hunger')
        thirst_stat = player_stats.get('thirst')

        health_core_stat = player_stats.get('health_core')
        energy_core_stat = player_stats.get('energy_core')
        power_core_stat = player_stats.get('power_core')
        hunger_core_stat = player_stats.get('hunger_core')
        thirst_core_stat = player_stats.get('thirst_core')

        if health_stat == 100:
            he_efix = 1
        else: he_efix = 0
        if energy_stat == 100:
            e_efix = 1
        else: e_efix = 0
        if power_stat == 100:
            p_efix = 1
        else: p_efix = 0
        if hunger_stat == 100:
            hu_efix = 1
        else: hu_efix = 0
        if thirst_stat == 100:
            t_efix = 1
        else: t_efix = 0


        if health_core_stat == 50:
            he_core_efix = 1
        else: he_core_efix = 0
        if energy_core_stat == 50:
            e_core_efix = 1
        else: e_core_efix = 0
        if power_core_stat == 50:
            p_core_efix = 1
        else: p_core_efix = 0
        if hunger_core_stat == 50:
            hu_core_efix = 1
        else: hu_core_efix = 0
        if thirst_core_stat == 50:
            t_core_efix = 1
        else: t_core_efix = 0


        self.health_coreframe_anim.tile_coordinate = [(9 - (health_stat % 10 - he_efix)), (health_stat // 10) - he_efix]
        self.energy_coreframe_anim.tile_coordinate = [(9 - (energy_stat % 10 - e_efix)), (energy_stat // 10) - e_efix]
        self.power_coreframe_anim.tile_coordinate  = [(9 - (power_stat % 10  - p_efix)),  (power_stat // 10)  - p_efix]
        self.hunger_coreframe_anim.tile_coordinate = [(9 - (hunger_stat % 10 - hu_efix)), (hunger_stat // 10) - hu_efix]
        self.thirst_coreframe_anim.tile_coordinate = [(9 - (thirst_stat % 10 - t_efix)), (thirst_stat // 10) - t_efix]

        self.health_core_bg_anim.tile_coordinate = [health_core_stat - he_core_efix,0]
        self.energy_core_bg_anim.tile_coordinate = [energy_core_stat - e_core_efix, 0]
        self.power_core_bg_anim.tile_coordinate = [power_core_stat - p_core_efix, 0]
        self.hunger_core_bg_anim.tile_coordinate = [hunger_core_stat - hu_core_efix, 0]
        self.thirst_core_bg_anim.tile_coordinate = [thirst_core_stat - t_core_efix, 0]

    def __init__(self, language_file, player_stats):
        self.language_file = language_file
        self.player_stats = player_stats
        self.minimap = Entity(texture = minimap, model = 'quad', position = (-0.68, -0.32, -0.05), scale = (0.4, 0.4, 0), alpha = 0, parent = camera.ui)

        self.dead_screen_status = 'none'

        # -------------------------------------------------------------------------------------------------------------
        # CORE GRAPHICS

        self.health_core = Entity(texture = core_spritesheet, model = 'quad', position = (-0.8255, -0.2285, -0.05), scale = (0.07, 0.07, 0), alpha = 0, parent = camera.ui, tileset_size = [5,1], tile_coordinate = [0,0])
        self.energy_core = Entity(texture = core_spritesheet, model = 'quad', position = (-0.768, -0.178, -0.05), scale = (0.07, 0.07, 0), alpha = 0, parent = camera.ui, tileset_size = [5, 1], tile_coordinate = [1, 0])
        self.power_core  = Entity(texture = core_spritesheet, model = 'quad', position = (-0.685, -0.161, -0.05), scale = (0.07, 0.07, 0), alpha = 0, parent = camera.ui, tileset_size = [5, 1], tile_coordinate = [2, 0])
        self.hunger_core = Entity(texture = core_spritesheet, model = 'quad', position = (-0.6, -0.178, -0.05), scale = (0.07, 0.07, 0), alpha = 0, parent = camera.ui, tileset_size = [5, 1], tile_coordinate = [3, 0])
        self.thirst_core = Entity(texture = core_spritesheet, model = 'quad', position = (-0.541, -0.2285, -0.05), scale = (0.07, 0.07, 0), alpha = 0, parent = camera.ui, tileset_size = [5,1], tile_coordinate = [4,0])


        # -> CORE FRAMES <- #

        self.health_coreframe_anim = Entity(texture = core_frame_spritesheet, model = 'quad', position = (self.health_core.x + 0.0005, self.health_core.y + 0.001, -0.1), scale = (0.07, 0.07, 0), alpha = 0, parent = camera.ui, tileset_size = [10,10])
        self.energy_coreframe_anim = Entity(texture = core_frame_spritesheet, model='quad', position=(self.energy_core.x + 0.0005, self.energy_core.y + 0.001, -0.1), scale=(0.07, 0.07, 0), alpha=0, parent=camera.ui, tileset_size=[10, 10])
        self.power_coreframe_anim = Entity(texture = core_frame_spritesheet, model='quad', position=(self.power_core.x + 0.0005, self.power_core.y + 0.001, -0.1), scale=(0.07, 0.07, 0), alpha=0, parent=camera.ui, tileset_size=[10, 10])
        self.hunger_coreframe_anim = Entity(texture = core_frame_spritesheet, model='quad', position=(self.hunger_core.x + 0.0005, self.hunger_core.y + 0.001, -0.1), scale=(0.07, 0.07, 0), alpha=0, parent=camera.ui, tileset_size=[10, 10])
        self.thirst_coreframe_anim = Entity(texture = core_frame_spritesheet, model='quad', position=(self.thirst_core.x + 0.0005, self.thirst_core.y + 0.001, -0.1), scale=(0.07, 0.07, 0), alpha=0, parent=camera.ui, tileset_size=[10, 10])

        self.health_coreframe_anim.tile_coordinate = [0,9]
        self.energy_coreframe_anim.tile_coordinate = [0, 9]
        self.power_coreframe_anim.tile_coordinate = [0, 9]
        self.hunger_coreframe_anim.tile_coordinate = [0, 9]
        self.thirst_coreframe_anim.tile_coordinate = [0, 9]

        # -------------------------------------------------------------------------------------------------------------
        # CORE BG SHEET

        self.health_core_bg_anim = Entity(texture = core_bg_spritesheet, model = 'quad', position = (self.health_core.x + 0.0005, self.health_core.y + 0.0005, 0.1), alpha = 0, parent = camera.ui, tileset_size = [50, 1], scale = (0.029,0.025))
        self.energy_core_bg_anim = Entity(texture = core_bg_spritesheet, model = 'quad', position = (self.energy_core.x + 0.0005, self.energy_core.y + 0.0015, 0.1), alpha = 0, parent = camera.ui, tileset_size = [50, 1], scale = (0.038,0.038))
        self.power_core_bg_anim = Entity(texture = core_bg_spritesheet, model = 'quad', position = (self.power_core.x + 0.0005, self.power_core.y + 0.001, 0.1), alpha = 0, parent = camera.ui, tileset_size = [50, 1], scale = (0.03,0.021))
        self.hunger_core_bg_anim = Entity(texture = core_bg_spritesheet, model = 'quad', position = (self.hunger_core.x + 0.0005, self.hunger_core.y + 0.002, 0.1), alpha = 0, parent = camera.ui, tileset_size = [50, 1], scale = (0.045,0.036))
        self.thirst_core_bg_anim = Entity(texture = core_bg_spritesheet, model = 'quad', position = (self.thirst_core.x + 0.0005, self.thirst_core.y + 0.001, 0.1), alpha = 0, parent = camera.ui, tileset_size = [50, 1], scale = (0.038,0.033))

        # 0,0 - Bal alsó
        # 9,4 - jobb felső

        self.health_core_bg_anim.tile_coordinate = [9, 4]
        self.energy_core_bg_anim.tile_coordinate = [9, 4]
        self.power_core_bg_anim.tile_coordinate = [9, 4]
        self.hunger_core_bg_anim.tile_coordinate = [9, 4]
        self.thirst_core_bg_anim.tile_coordinate = [9, 4]

        # -------------------------------------------------------------------------------------------------------------
        # DEATH SCREEN

        self.dead_screen_bg = Entity(color = color.black, parent = camera.ui, position = (0,0,0), scale = (2,1,0), alpha = 0, model='quad')
        self.dead_screen_anim = SpriteSheetAnimation(dead_screen_spritesheet, alpha = 0,parent = camera.ui, tileset_size=(30, 2), position = (0,0.12,-0.1), scale=(0.373, 0.177), fps = 30, animations={
                'show_dead_screen': ((0, 0), (29, 0)),
                'hide_dead_screen': ((0, 1), (29, 1)),
                'static_hide': ((29, 1), (29, 1)),
                'static_show': ((29, 0), (29, 0))})

        self.dead_continue_text = Text(text = '', position=[0.74, -0.44, -0.01], color = color.black, parent=camera.ui, font='fonts/CHINESER.TTF', scale = [1.3, 1.1, 0])
        self.dead_continue_click = Entity(alpha=0, scale=(0.15, 0.05, 0), position=[0.79, -0.448, 0], model='quad', collider='box', parent=camera.ui, on_click=Func(HUD.hide_death_screen, self), on_mouse_enter=Func(HUD.dead_continue_hover, self), on_mouse_exit=Func(HUD.dead_continue_leave, self))
        self.dead_continue_click.disable()

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////// #

    def show_hud(self):
        self.minimap.fade_in(value=0.9, duration=0.4, delay = 0.1)

        self.health_core.fade_in(value=1, duration=0.3, delay=0.02)
        self.energy_core.fade_in(value=1, duration=0.3, delay=0.02)
        self.power_core.fade_in(value=1, duration=0.3, delay=0.02)
        self.hunger_core.fade_in(value=1, duration=0.3, delay=0.02)
        self.thirst_core.fade_in(value=1, duration=0.3, delay=0.02)

        self.health_coreframe_anim.fade_in(value=0.9, duration=0.4, delay=0.1)
        self.energy_coreframe_anim.fade_in(value=0.9, duration=0.4, delay=0.1)
        self.power_coreframe_anim.fade_in(value=0.9, duration=0.4, delay=0.1)
        self.hunger_coreframe_anim.fade_in(value=0.9, duration=0.4, delay=0.1)
        self.thirst_coreframe_anim.fade_in(value=0.9, duration=0.4, delay=0.1)

        self.health_core_bg_anim.fade_in(value=0.9, duration=0.4, delay=0.1)
        self.energy_core_bg_anim.fade_in(value=0.9, duration=0.4, delay=0.1)
        self.power_core_bg_anim.fade_in(value=0.9, duration=0.4, delay=0.1)
        self.hunger_core_bg_anim.fade_in(value=0.9, duration=0.4, delay=0.1)
        self.thirst_core_bg_anim.fade_in(value=0.9, duration=0.4, delay=0.1)


    def hide_hud(self, speed = 0.12):
        self.minimap.fade_in(value=0, duration=speed, delay = 0.05)

        self.health_core.fade_in(value=0, duration=speed, delay = 0.05)
        self.energy_core.fade_in(value=0, duration=speed, delay=0.05)
        self.power_core.fade_in(value=0, duration=speed, delay=0.05)
        self.hunger_core.fade_in(value=0, duration=speed, delay=0.05)
        self.thirst_core.fade_in(value=0, duration=speed, delay=0.05)

        self.health_coreframe_anim.fade_in(value=0, duration=speed, delay=0.05)
        self.energy_coreframe_anim.fade_in(value=0, duration=speed, delay=0.05)
        self.power_coreframe_anim.fade_in(value=0, duration=speed, delay=0.05)
        self.hunger_coreframe_anim.fade_in(value=0, duration=speed, delay=0.05)
        self.thirst_coreframe_anim.fade_in(value=0, duration=speed, delay=0.05)

        self.health_core_bg_anim.fade_in(value=0, duration=speed, delay=0.05)
        self.energy_core_bg_anim.fade_in(value=0, duration=speed, delay=0.05)
        self.power_core_bg_anim.fade_in(value=0, duration=speed, delay=0.05)
        self.hunger_core_bg_anim.fade_in(value=0, duration=speed, delay=0.05)
        self.thirst_core_bg_anim.fade_in(value=0, duration=speed, delay=0.05)

    def send_player_stats(self, player_stats):
        self.player_stats = player_stats


########################################################################################################################
# INVENTORY #


class Inventory(Entity):
    def __init__(self, language_pack, **kwargs):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            texture = None,
            texture_scale = (4,4),
            scale = (.43, .43),
            origin = (-.5, .5),
            position = (-0.24,0.275),
            color = color.color(0,0,.1,.9))

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.language_pack = language_pack
        self.background = Entity(texture = inventory_background, alpha = 1, scale = (0.62, 1.024, -0.12), position=[0, 0, 0], model='quad', parent=camera.ui)


    # [] ------------------------------------------------------------------------------------------------------------- []

    def find_free_spot(self): # Keres egy üres helyet, és visszadja az x, y koordinátáját.
        for y in range(4):
            for x in range(4):
                grid_positions = [(int(e.x*self.texture_scale[0]), int(e.y*self.texture_scale[1])) for e in self.children]

                if not (x,-y) in grid_positions:
                    return x, y

    # [] ------------------------------------------------------------------------------------------------------------- []

    def append(self, item, x=0, y=0): # Hozzáad egy itemet
        if len(self.children) >= 4*4: # Lefut, ha tele az inventory
            print('inventory full')
            return

        x, y = self.find_free_spot() # De előtte keresni kel legy szabad helyet.

        icon = Draggable( parent = self, model = 'quad', texture = item, color = color.white,
            scale_x = 1 / self.texture_scale[0], scale_y = 1 / self.texture_scale[1], origin = (-.5,.5),
            x = x * 1 / self.texture_scale[0], y = -y * 1 / self.texture_scale[1], z = -.5)

        name = item.replace('_', ' ').title()

        # [] --------------------------------------------------------------------------------------------------------- []

        def drag():
            icon.org_pos = (icon.x, icon.y)
            icon.z -= .01   # azért, hogy a megragadott item a többi réteg felett legyen

        def drop():
            icon.x = int((icon.x + (icon.scale_x/2)) * 4) / 4
            icon.y = int((icon.y - (icon.scale_y/2)) * 4) / 4
            icon.z += .01

            # Ha rossz helyre húzta kerüljön vissza az eredeti helyére.
            if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                icon.position = (icon.org_pos)
                return

            # Ha a pozíció foglalt, cseréljenek helyet
            for c in self.children:
                if c == icon:
                    continue

                if c.x == icon.x and c.y == icon.y:
                    c.position = icon.org_pos

        icon.drag = drag
        icon.drop = drop

    def show_inventory(self):
        pass

    def hide_inventory(self):
        pass

























