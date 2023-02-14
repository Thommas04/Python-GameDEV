
# REDNOTE - HUD
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] #

from ursina import *

# WEAPON WHEEL # ---------------------------------------------------*

weapon_wheel = 'hud/weapon_wheel/weapon_wheel.png'
wheelbar_selected = 'hud/weapon_wheel/wheel_choosen.png'
wheelbar_selector = 'hud/weapon_wheel/wheel_selected.png'

# AMMO AND MONEY ICONS

screen_icons = 'hud/hud_widgets/screen_icons/screen_icons.png'

# ICONS

spencer_carbine_icon = 'hud/weapon_wheel_items/rifle_icon.png'
hand_icon = 'hud/weapon_wheel_items/hand_icon.png'
colt_icon = 'hud/weapon_wheel_items/revolver_icon.png'
axe_icon = 'hud/weapon_wheel_items/axe_icon.png'
lantern_icon = 'hud/weapon_wheel_items/lantern_icon.png'

# DEAD SCREEN # ------------------------------------------------------------*

dead_screen_spritesheet = 'hud/death_screen/death_screen_sheet.png'


# HUD # ------------------------------------------------------------*

minimap = 'hud/hud_widgets/minimap/minimap_frame.png'
minimap_background = 'hud/hud_widgets/minimap/minimap_bg.png'

core_frame_spritesheet = 'hud/hud_widgets/cores/core_frame_sheet.png'
core_spritesheet = 'hud/hud_widgets/cores/core_sheet.png'
core_bg_spritesheet = 'hud/hud_widgets/cores/core_bg_sheet.png'

# INVENTORY # ------------------------------------------------------------*

inventory_background = 'hud/inventory/widgets/inventory_bg.png'
inventory_buttons_spritesheet = 'hud/inventory/widgets/inventory_buttons_sheet.png'
inventory_hovered_tile = 'hud/inventory/widgets/inventory_hover.png'
inventory_selected_tile = 'hud/inventory/widgets/inventory_selected.png'
amount_bg = 'hud/inventory/widgets/amount_bg.png'

# ATTACK HUD / WAVES# ------------------------------------------------------------*

attack_hud_bg = 'hud/hud_widgets/attack/attack_bg.png'
enemy_bar = 'hud/hud_widgets/attack/enemy_number_bar.png'
wave_completed = 'hud/hud_widgets/attack/wave_done.png'
wave_base = 'hud/hud_widgets/attack/wave.png'

# SHOP # -------------------------------------------------------------------------*

shop_bg = 'hud/shop/select_menu.png'
bars_sheet = 'hud/shop/shop_bars.png'

# BUILDER MODE # ------------------------------------------------------------*

grid = 'hud/builder_mode_hud/grid.png'

# INSTRUCTIONS # ------------------------------------------------------------*

separator_line = 'hud/hud_widgets/instructions/separator_line.png'

instructions_opened = False

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

        self.tile_selected = Entity(texture = wheelbar_selector, rotation = (0,0,0), model = 'quad', position = (0.202, -0.021, -0.1), scale = (-0.25, -0.3, 0), alpha = 0, parent = camera.ui)


        self.up_icon = Entity(tag = '', texture = hand_icon, model = 'quad', position = (0, 0.245, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)
        self.upper_left_icon = Entity(tag = 'colt', rotation = (0,0,-40), texture = colt_icon, model = 'quad', position = (-0.168, 0.175, -0.1), scale = (0.165, 0.165, 0), alpha = 0, parent=camera.ui)
        self.upper_right_icon = Entity(tag = '', texture = hand_icon, model = 'quad', position = (0.2, 0.15, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)

        self.right_icon = Entity(tag = 'hand', texture = hand_icon, model = 'quad', position = (0.275, -0.022, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)
        self.left_icon = Entity(tag = '', texture = axe_icon, model = 'quad', position = (-0.26, -0.03, -0.1), scale = (0.12, 0.12, 0), rotation = (0,0,-69), alpha = 0, parent=camera.ui)
        self.lower_left_icon = Entity(tag = '', texture = hand_icon, model = 'quad', position = (-0.17, -0.22, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)
        self.lower_right_icon = Entity(tag = '', texture = hand_icon, model = 'quad', position = (0.2, -0.21, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)
        self.down_icon = Entity(tag = '', texture = hand_icon, model = 'quad', position = (0.02, -0.295, -0.1), scale = (0.14, 0.14, 0), alpha = 0, parent=camera.ui)


        self.wheel_icons_list = [self.right_icon, self.upper_left_icon, self.left_icon]#, self.up_iconself.upper_right_icon, self.lower_left_icon, self.lower_right_icon, self.down_icon]

    def get_back_selected_wheeltile(self):
        return self.selected_tile


    def show_weaponwheel(self):
        self.wheel.fade_in(value=0.85, duration=0.15, delay = 0)
        self.tile_selected.fade_in(value=0.85, duration=0.15, delay = 0)
        self.pause_menu.filters.setBlurSharpen(amount=0)
        for i in self.weapon_wheel_list:
            i.enable()
        for icon in self.wheel_icons_list:
            icon.fade_in(value=0.5, duration=0.15, delay = 0)

    def hide_weaponwheel(self):
        self.wheel.fade_in(value=0, duration=0.15, delay = 0)
        self.tile_selected.fade_in(value=0, duration=0.15, delay=0)
        self.pause_menu.filters.setBlurSharpen(amount=1)
        for i in self.weapon_wheel_list:
            i.disable()
        for icon in self.wheel_icons_list:
            icon.fade_in(value=0, duration=0.15, delay = 0)

########################################################################################################################
# HUD / CORES & Minimap #


class HUD(Entity):

    def show_money_text(self, cash_bank, cash_hand):
        money_bank = str(cash_bank).split('.')
        money_hand = str(cash_hand).split('.')

        if len(money_bank) == 1:
            money_bank = [cash_bank, '00']
        if len(money_hand) == 1:
            money_hand = [cash_hand, '00']

        if len(money_hand[1]) == 1:
            money_hand[1] = '0' + money_hand[1]

        if len(money_bank[1]) == 1:
            money_bank[1] = '0' + money_bank[1]

        self.cash_inhand.text = '$' + str(money_bank[0])
        self.cash_inhand_cents.text = money_bank[1]

        self.cash_inbank.text = '$' + str(money_hand[0])
        self.cash_inbank_cents.text = money_hand[1]

        self.cash_inbank_icon.alpha = 1
        self.cash_inhand_icon.alpha = 1

        self.cash_inhand_cents_shadow.text = money_hand[1]
        self.cash_inbank_cents_shadow.text = money_bank[1]
        self.cash_inhand_shadow.text = '$' + str(money_hand[0])
        self.cash_inbank_shadow.text = '$' + str(money_bank[0])

    def hide_money_text(self):
        self.cash_inhand.text = ''
        self.cash_inhand_cents.text = ''

        self.cash_inbank.text = ''
        self.cash_inbank_cents.text = ''

        self.cash_inbank_icon.alpha = 0
        self.cash_inhand_icon.alpha = 0

        self.cash_inhand_cents_shadow.text = ''
        self.cash_inbank_cents_shadow.text = ''
        self.cash_inhand_shadow.text = ''
        self.cash_inbank_shadow.text = ''





    # --------------------------------------------------------

    def hide_ammo_text(self):
        self.ammo_loaded.text = ''
        self.ammo_loaded_shadow.text = ''
        self.ammo_remain.text = ''
        self.ammo_remain_shadow.text = ''
        self.bullet_icon.alpha = 0

    def show_ammo_text(self, revolver_ammo, full_ammo):
        self.ammo_loaded.text = revolver_ammo
        self.ammo_loaded_shadow.text = revolver_ammo
        self.ammo_remain.text = full_ammo
        self.ammo_remain_shadow.text = full_ammo
        self.bullet_icon.alpha = 1

    # --------------------------------------------------------

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
        invoke(HUD.delayed_hide_deadscreen_bg, self, delay=0.9)

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
        HUD.hide_instruction_slots(self)

    def hide_death_screen(self):
        self.dead_continue_text.text = ''
        self.dead_continue_text.color = color.black
        self.dead_continue_click.disable()
        self.death_text.text = ''
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

    # ------------------------------------------------------------------------------------------------------------------
    #TODO

    def update_attack_hud(self, enemy_alive, existing_enemy, wave_amount, current_wave):
        self.enemy_amount_txt.text = f'{enemy_alive} / {existing_enemy}'
        self.waves_amount_txt.text = f'{current_wave} / {wave_amount}'


    def delayed_show_attack_hud(self):
        self.enemy_txt.text = self.language_file[3]['Enemy']
        self.waves_txt.text = self.language_file[3]['Wave']
        self.enemy_txt.appear(speed=.05, delay=0)
        self.waves_txt.appear(speed=.05, delay=0)

    def show_attack_hud(self):
        self.attack_bg.fade_in(value = 0.9, duration = 0.4, delay = 0.2)
        self.enemy_amount_txt.fade_in(value = 1, duration = 0.4, delay = 0.4)
        self.waves_amount_txt.fade_in(value = 1, duration = 0.4, delay = 0.4)
        invoke(HUD.delayed_show_attack_hud, self, delay = 0.85)
        #self.enemy_number_bar.fade_in(value = 1, duration = 0.4, delay = 0.4)

    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    def hide_attack_hud(self):
        self.attack_bg.fade_out(value = 0, duration = 0.2, delay = 0.1)
        #self.enemy_number_bar.fade_in(value=0, duration=0.2, delay=0.1)
        self.enemy_txt.fade_out(value = 0, duration = 0.2, delay = 0.1)
        self.waves_txt.fade_out(value = 0, duration = 0.2, delay = 0.1)
        self.enemy_amount_txt.fade_out(value = 0, duration = 0.2, delay = 0.1)
        self.waves_amount_txt.fade_out(value = 0, duration = 0.2, delay = 0.1)

    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    #TODO
    def show_instruction_slots(self, instruction_type):
        global instructions_opened
        if instructions_opened == False:
            self.separator_line.fade_in(value=1, delay=0.1, duration=0.2)
            self.instruction_title.fade_in(value=1, delay=0.1, duration=0.2)
            self.instruction_title_shadow.fade_in(value=1, delay=0.1, duration=0.2)

            if instruction_type == 'shop_marker':
                self.instruction_title.text = self.instruction_title_shadow.text = self.language_file[4]['SHOP']

                self.instruction_slots[0].text = self.instruction_slots_shadows[0].text = f'{self.language_file[4]["SELL"]} - E'
                self.instruction_slots[1].text = self.instruction_slots_shadows[1].text = f'{self.language_file[4]["BUY"]} - Q'

                for i in range(2):
                    self.instruction_slots[i].fade_in(value=1, delay=0.1, duration=0.2)
                    self.instruction_slots_shadows[i].fade_in(value = 1, delay = 0.1, duration = 0.2)



            instructions_opened = True

    #-------------------------------------------------------------------------------------------------------------------
    def hide_instruction_slots(self):
        global instructions_opened
        if instructions_opened == True:
            for instruction_slot in self.instruction_slots:
                instruction_slot.fade_out(value = 0, delay = 0.1, duration = 0.2)
            for instruction_slot_sh in self.instruction_slots_shadows:
                instruction_slot_sh.fade_out(value = 0, delay = 0.1, duration = 0.2)

            self.separator_line.fade_out(value = 0, delay = 0.1, duration = 0.2)
            self.instruction_title.fade_out(value = 0, delay = 0.1, duration = 0.2)
            self.instruction_title_shadow.fade_out(value = 0, delay = 0.1, duration = 0.2)

            instructions_opened = False

    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #SHOP HOVER

    def shop_click(self):
        self.shop_bars.tile_coordinate = [0,1]
        self.shop_selector.alpha = 1

        if self.player.player_stats['bank_balance'] >= 321:
            self.player.amount_of_tower += 1
            self.player.player_stats['bank_balance'] -= 320.99
            HUD.show_money_text(self, self.player.player_stats['bank_balance'], self.player.player_stats['wallet_balance'])

    def shop_hover(self):
        self.shop_bars.tile_coordinate = [0,0]

    def shop_leave(self):
        self.shop_bars.tile_coordinate = [0,1]


    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    def __init__(self, language_file, player):
        self.language_file = language_file
        self.player = player
        self.minimap = Entity(texture = minimap, model = 'quad', position = (-0.68, -0.32, -0.05), scale = (0.4, 0.4, 0), alpha = 0, parent = camera.ui)
        self.minimap_bg = Entity(texture = minimap_background, model = 'circle', position = (-0.685, -0.326, -0.04), scale = (0.24, 0.24), alpha = 0, parent = camera.ui, texture_scale = (4,4))

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
        self.death_text = Text(text='', position=[0, 0.08, -0.02], color=rgb(172, 174, 190), parent=camera.ui, font='fonts/CHINESER.TTF', scale=1)
        self.dead_continue_text = Text(text = '', position=[0.7, -0.44, -0.01], color = color.black, parent=camera.ui, font='fonts/CHINESER.TTF', scale = [1.3, 1.1, 0])
        self.dead_continue_click = Entity(alpha=0, scale=(0.15, 0.05, 0), position=[0.79, -0.448, 0], model='quad', collider='box', parent=camera.ui, on_click=Func(HUD.hide_death_screen, self), on_mouse_enter=Func(HUD.dead_continue_hover, self), on_mouse_exit=Func(HUD.dead_continue_leave, self))
        self.dead_continue_click.disable()

        # -------------------------------------------------------------------------------------------------------------
        # PRINT MONEY AND AMMO

        self.ammo_remain_shadow = Text(text = '', position=[0.782, 0.453, -0.03], color = color.black, parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1)
        self.ammo_loaded_shadow = Text(text = '', position=[0.778, 0.435, -0.03], origin=(0.5, 0), color = color.black, parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1.4)


        self.ammo_remain = Text(text = '', position=[0.78, 0.455, -0.04], color = rgb(172,174,190), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1)
        self.ammo_loaded = Text(text = '', position=[0.775, 0.438, -0.04], origin=(0.5, 0), color = rgb(198,205,205), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1.4)
        self.bullet_icon = Entity(texture = screen_icons, model='quad', position = [0.84, 0.439, -0.01], alpha=0, parent=camera.ui, tileset_size=[3, 1], tile_coordinate = [2,0],  scale=(0.05, 0.05))

        # -----[]

        self.cash_inhand_cents_shadow = Text(text = '', position=[0.779, 0.453, -0.03], color = color.black, parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1)
        self.cash_inbank_cents_shadow = Text(text = '', position=[0.779, 0.403, -0.03], color = color.black, parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1)
        self.cash_inhand_shadow = Text(text = '', position=[0.773, 0.435, -0.03], color = color.black, origin=(0.5, 0), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1.4)
        self.cash_inbank_shadow = Text(text = '', position=[0.773, 0.385, -0.03], color = color.black, origin=(0.5, 0), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1.4)


        self.cash_inhand_cents = Text(text = '', position=[0.775, 0.405, -0.04], color = rgb(172,174,190), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1)
        self.cash_inbank_cents = Text(text = '', position=[0.775, 0.455, -0.04], color = rgb(172,174,190), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1)

        self.cash_inhand = Text(text = '', position=[0.77, 0.388, -0.04], color = rgb(198,205,205), origin=(0.5, 0), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1.4)
        self.cash_inbank = Text(text = '', position=[0.77, 0.438, -0.04], color = rgb(198,205,205), origin=(0.5, 0), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1.4)

        self.cash_inbank_icon = Entity(texture = screen_icons, model='quad', position = [0.84, 0.44, -0.03], alpha=0, parent=camera.ui, tileset_size=[3, 1], tile_coordinate = [0,0],  scale=(0.05, 0.05))
        self.cash_inhand_icon = Entity(texture = screen_icons, model='quad', position = [0.84, 0.39, -0.03], alpha=0, parent=camera.ui, tileset_size=[3, 1], tile_coordinate = [1,0],  scale=(0.05, 0.05))

        # -------------------------------------------------------------------------------------------------------------
        # Attack Waves TODO

        self.waves_txt = Text(alpha = 0, text = '', position=[-0.2, 0.43, -0.02], color = rgb(172,174,190), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1)
        self.waves_amount_txt = Text(alpha = 0, text = '', position=[-0.1, 0.43, -0.02], color = rgb(172,174,190), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1)
        self.enemy_txt = Text(alpha = 0,text = '', position=[-0.12, 0.382, -0.02], origin = (0.5,0),color = rgb(172,174,190), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1)
        self.enemy_amount_txt = Text(alpha = 0,text = '', position=[-0.03, 0.382, -0.02], origin = (0.5,0),color = rgb(172,174,190), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1)

        self.attack_bg = Entity(texture = attack_hud_bg, model='quad', position = [0, 0.4, -0.01], alpha=0, parent=camera.ui, scale=(0.55, 0.19))


        #self.enemy_number_bar = Entity(texture = enemy_bar, model='quad', position = [0.03, 0.38, -0.01], alpha=0, parent=camera.ui, scale=(0.290, 0.013))

        # -------------------------------------------------------------------------------------------------------------
        # INSTRUCTION SLOTS

        self.instruction_slots = []
        self.instruction_slots_shadows = []
        self.instruction_keys = []

        self.separator_line = Entity(texture = separator_line, model = 'quad', origin=(0.5, 0), position = (0.87, -0.445, -0.04), scale = (0.22, 0.016), alpha = 0, parent = camera.ui)
        self.instruction_title = Text(text='', position=[0.82, -0.475, -0.2], origin=(0.5, 0), color=rgb(140, 174, 190), parent=camera.ui, font='fonts/CHINESER.TTF', scale=1.1)
        self.instruction_title_shadow = Text(text='', position=[0.823, -0.478, -0.15], origin=(0.5, 0), color=rgb(2, 2, 2), parent=camera.ui, font='fonts/CHINESER.TTF', scale=1.1)

        for i in range(5):
            self.instruction_slot = Text(text='', position=[0.82, -0.42 + (i * 0.03) , -0.2], origin=(0.5, 0), color=rgb(172, 174, 190), parent=camera.ui, font='fonts/CHINESER.TTF', scale=1.1)
            self.instruction_slot_shadow = Text(text='', position=[0.823, -0.423 + (i * 0.03), -0.15], origin=(0.5, 0), color=rgb(2, 2, 2), parent=camera.ui, font='fonts/CHINESER.TTF', scale=1.1)
            self.instruction_slots.append(self.instruction_slot)
            self.instruction_slots_shadows.append(self.instruction_slot_shadow)

        # -------------------------------------------------------------------------------------------------------------
        # SHOP

        self.shop_bars = Entity(texture=bars_sheet, model='quad', position=(-0.55, 0.25, -0.06), scale=(0.48, 0.09, 0), alpha=0, parent=camera.ui, tileset_size=[1, 3], tile_coordinate=[0, 1])
        self.shop_selector = Entity(texture=bars_sheet, model='quad', position=(-0.55, 0.25, -0.07), scale=(0.48, 0.09, 0), alpha=0, parent=camera.ui, tileset_size=[1, 3], tile_coordinate=[0, 2])
        self.shop_bg = Entity(texture = shop_bg, model='quad', position=(-0.54, 0, -0.05), scale=(0.57, 0.88, 0), alpha=0, parent=camera.ui)

        self.shop_first_clickable = Entity(model='quad', position=(-0.54, 0.25, -0.08), scale=(0.48, 0.07, 0), alpha=0, collider = 'box', parent=camera.ui, on_click=Func(HUD.shop_click, self), on_mouse_enter=Func(HUD.shop_hover, self), on_mouse_exit=Func(HUD.shop_leave, self))
        self.shop_first_clickable.disable()

        self.shop_text = Text(text = 'Torony', position=(-0.75, 0.26, -0.09), color = rgb(172,174,190), parent=camera.ui, font='fonts/CHINESER.TTF', scale = 1.1)
        self.price_text = Text(text='$320.99', position=(-0.45, 0.26, -0.09), origin = (-0.5, 0.5), color=rgb(172, 174, 190), parent=camera.ui, font='fonts/CHINESER.TTF', scale=1.1)

        self.shop_text.alpha = 0
        self.price_text.alpha = 0

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////// #

    def show_shop(self):
        self.shop_bars.fade_in(value = 1, delay = 0.12, duration = 0.1)
        self.shop_bg.fade_in(value = 1, delay = 0.1, duration = 0.1)
        self.shop_text.fade_in(value = 1, delay = 0.1, duration = 0.1)
        self.price_text.fade_in(value = 1, delay = 0.1, duration = 0.1)
        self.shop_first_clickable.enable()

    def hide_shop(self):
        self.shop_bars.fade_out(value=0, delay=0.12, duration=0.1)
        self.shop_selector.fade_out(value=0, delay=0.12, duration=0.1)
        self.shop_bg.fade_out(value=0, delay=0.1, duration=0.1)
        self.shop_text.fade_out(value=0, delay=0.1, duration=0.1)
        self.price_text.fade_out(value=0, delay=0.1, duration=0.1)
        self.shop_first_clickable.disable()

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////// #

    def show_hud(self):
        self.minimap.fade_in(value=1, duration=0.4, delay = 0.1)
        self.minimap_bg.fade_in(value=0.9, duration=0.4, delay = 0.1)

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
        print('mukukogy')

    def hide_hud(self, speed = 0.12):
        self.minimap.fade_in(value=0, duration=speed, delay = 0.05)
        self.minimap_bg.fade_in(value=0, duration=speed, delay = 0.05)

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

        HUD.hide_instruction_slots(self)
        HUD.hide_money_text(self)
        HUD.hide_ammo_text(self)
        HUD.hide_attack_hud(self)

    def send_player_stats(self, player_stats):
        self.player_stats = player_stats





########################################################################################################################
# INVENTORY #


dict_x = {0.75 : 3, 0.5 : 2, 0.25 : 1, 0.0 : 0}
dict_y = {-0.75 : 0, -0.5 : 1, -0.25 : 2, 0.0 : 3}

sell_table = {'bag' : 120.99,
              'wooden_plank' : 22.30
              }

class Inventory(Entity):
    def mouse_hover_invslot(self, position):
        self.highlighted_tile.position = [position[0] + 0.005, position[1], position[2]]
        self.highlighted_tile.alpha = 1

    def draggable_mouse_hover(self, x, y, mouse):
        try:
            if not mouse:
                self.highlighted_tile.position = [self.position.x + 0.108 * dict_x[x] + 0.055, self.position.y + 0.108 * dict_y[y] - 0.38, -0.1]
                self.highlighted_tile.alpha = 1
            else:
                self.highlight_click_tile.position = [self.position.x + 0.108 * dict_x[x] + 0.055, self.position.y + 0.108 * dict_y[y] - 0.38, -0.1]
                self.highlight_click_tile.alpha = 1
                self.highlighted_tile.alpha = 0
        except:
            pass

    # Ha kétszer megnyomod a balklikket valamelyik itemen. [ITEM HASZNÁLAT]
    def draggable_mouse_double_click(self, tag): # TODO tag[0] = Tárgy neve ; tag[1] = kategória ; tag[2] = darabszám ; tag[3] = tradeable
        for child in self.children:
            if child.tag[0] == tag[0]:

                if tag[1] in ('food', 'healthcare'):
                    if self.mode == 'basic':
                        child.tag[2] -= 1

                        if tag[0] == 'meat':
                            if self.player.player_stats['hunger_core'] < 50:
                                self.player.player_stats['hunger_core'] += 15
                            if self.player.player_stats['hunger_core'] == 50:
                                self.player.player_stats['hunger'] += 15

                    if self.mode == 'sell':
                        if tag[3] == True: #tradeable == True
                            child.tag[2] -= 1
                            self.player.player_stats['wallet_balance'] += sell_table[tag[0]]
                            self.hud.show_money_text(self.player.player_stats['bank_balance'], self.player.player_stats['wallet_balance'])


                # child.children[0] -> entity bg, [1] -> text
                child.children[1].text = child.tag[2]

                if child.tag[2] <= 1:
                    child.children[0].visible = False
                    child.children[1].visible = False

                if child.tag[2] >= 2:
                    child.children[0].visible = True
                    child.children[1].visible = True

                if child.tag[2] <= 0:
                    self.highlight_click_tile.alpha = 0
                    destroy(child)
        print(child.tag[0])


    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, pause_menu, player, hud, **kwargs):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            texture = None,
            texture_scale = (4,4),
            scale = (.43, .43),
            origin = (-.5, .5),
            position = (-0.24,0.275),
            color = color.color(0,0,.1,.9),
            alpha = 0,
            visible = False)

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.player = player
        self.hud = hud
        self.pause_menu = pause_menu
        self.background = Entity(texture = inventory_background, alpha = 0, scale = (0.62, 1.024, -0.12), position=[self.position[0] + 0.24, 0, 0], model='quad', parent=camera.ui)

        # for hovered
        self.highlighted_tile = Entity(texture = inventory_hovered_tile, alpha = 0, scale = (0.116, 0.12, 0), position=[0, 0, 0], model='quad', parent=camera.ui)
        # for clicked
        self.highlight_click_tile = Entity(texture = inventory_selected_tile, alpha = 0, scale = (0.116, 0.12, 0), position=[0, 0, 0], model='quad', parent=camera.ui)

        inv_x = [0,1,2,3]
        inv_y = [0,1,2,3]

        self.nums_bg_list = []
        self.inventory_clicks_list = []
        for x in inv_x:
            for y in inv_y:
                self.inventory_clicks = Entity(alpha = 0, scale = 0.1, position = [self.position.x + 0.108 * x + 0.05, self.position.y + 0.108 * y - 0.38, -0.1], model='quad', collider='box', parent=camera.ui, on_mouse_enter=Func(Inventory.mouse_hover_invslot, self, [self.position.x + 0.108 * x + 0.05, self.position.y + 0.108 * y - 0.38, -0.04]) )
                self.inventory_clicks_list.append(self.inventory_clicks)

        for click in self.inventory_clicks_list:
            click.disable()





    # [] ------------------------------------------------------------------------------------------------------------- []

    def find_free_spot(self, tagged): # Keres egy üres helyet, és visszadja az x, y koordinátáját.
        for y in range(4):
            for x in range(4):

                self.new_children_list = []
                for i in self.children:
                    if i.tag[1] == tagged:
                        self.new_children_list.append(i)

                self.grid_positions = [(int(e.x*self.texture_scale[0]), int(e.y*self.texture_scale[1])) for e in self.new_children_list]

                if not (x,-y) in self.grid_positions:
                    return x, y

    # [] ------------------------------------------------------------------------------------------------------------- []

    def remove(self, name, category):
        for item in self.children:
            destroy(item)

    def append(self, item, tagged, amount, tradeable, x = 0, y = 0): # Hozzáad egy itemet
        if len(self.children) >= 4*4: # Lefut, ha tele az inventory
            print('inventory full')
            return

        x, y = self.find_free_spot(tagged) # De előtte keresni kell egy szabad helyet.

        icon = Draggable(alpha = 0, parent = self, model = 'quad', texture = item, color = color.white,
            scale_x = 1 / self.texture_scale[0], scale_y = 1 / self.texture_scale[1], origin = (-.5,.5),
            x = x * 1 / self.texture_scale[0], y = -y * 1 / self.texture_scale[1], z = -.5, tag = [item, tagged, amount],
            on_mouse_enter = Func(Inventory.draggable_mouse_hover, self, x = x * 1 / self.texture_scale[0], y = -y * 1 / self.texture_scale[1], mouse = False),
            on_click = Func(Inventory.draggable_mouse_hover, self, x = x * 1 / self.texture_scale[0], y = -y * 1 / self.texture_scale[1], mouse = True),
            on_double_click = Func(Inventory.draggable_mouse_double_click, self, tag = [item, tagged, amount, tradeable]))


        self.amount_background = Entity(texture = amount_bg, alpha = 0, model='quad', origin = (1,1), scale=(0.44, 0.44, 0), position = [1.2, -0.3, -0.1], parent=icon)
        self.amount_txt = Text(text = amount, origin = (0,0), position = [0.75, -0.77, -0.12], color=rgb(40,40,40), parent=icon, font='fonts/CHINESER.TTF', scale=10)
        self.amount_background.visible = False
        self.amount_txt.visible = False

        self.nums_bg_list.append(self.amount_background)
        self.nums_bg_list.append(self.amount_txt)

        for bgs in self.nums_bg_list:
            bgs.alpha = 0

        if amount > 1:
            self.amount_background.visible = True
            self.amount_txt.visible = True

        icon.disable()

        name = item.replace('_', ' ').title()

        # [] --------------------------------------------------------------------------------------------------------- []

        def drag():
            icon.org_pos = (icon.x, icon.y)
            icon.z = -0.3 # azért, hogy a megragadott item a többi réteg felett legyen
            icon.children[0].z = -0.112
            icon.children[1].z = -0.114
        def drop():
            icon.x = int((icon.x + (icon.scale_x / 2)) * 4) / 4
            icon.y = int((icon.y - (icon.scale_y / 2)) * 4) / 4
            icon.z = -0.1
            icon.children[0].z = -0.105
            icon.children[1].z = -0.108

            icon.on_mouse_enter = Func(Inventory.draggable_mouse_hover, self, x = icon.x, y = icon.y, mouse = False)
            icon.on_click = Func(Inventory.draggable_mouse_hover, self, x = icon.x, y = icon.y, mouse = True)
            try:
                self.highlight_click_tile.position = [self.position.x + 0.108 * dict_x[icon.position.x] + 0.055, self.position.y + 0.108 * dict_y[icon.position.y] - 0.38, -0.1]
            except: print('Key Error : Nincs a szótárban')

            # Ha rossz helyre húzta kerüljön vissza az eredeti helyére.
            if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                icon.position = (icon.org_pos)
                self.highlight_click_tile.alpha = 0
                return

            # Ha a pozíció foglalt, cseréljenek helyet
            for c in self.children:
                if c == icon:
                    continue

                if c.tag[1] == icon.tag[1]:
                    if c.x == icon.x and c.y == icon.y:
                        c.position = icon.org_pos
                        c.on_mouse_enter = Func(Inventory.draggable_mouse_hover, self, x=c.x, y=c.y, mouse=False)
                        c.on_click = Func(Inventory.draggable_mouse_hover, self, x=c.x, y=c.y, mouse=True)
                        self.highlight_click_tile.position = [self.position.x + 0.108 * dict_x[icon.position.x] + 0.055, self.position.y + 0.108 * dict_y[icon.position.y] - 0.38, -0.1]

        icon.drag = drag
        icon.drop = drop

    def hide_items_delay(self, item):
        item.disable()

    def show_items_delay(self, item):
        item.enable()

    def show_inventory(self, x, mode):
        self.mode = mode # beállítja hogy milyen módban lett megnyitva az inventory (sell / basic)
        self.visible = True
        self.position = (x, self.position.y, self.position.z)
        self.background.position = (x + 0.24, self.background.position.y, self.background.position.z)

        self.pause_menu.filters.setBlurSharpen(amount=0)
        self.background.fade_in(value=1, duration=0.3, delay=0.02)
        for item in self.children:
            item.fade_in(value=1, duration=0.3, delay=0.02)
            invoke(Inventory.show_items_delay, self, item, delay = 0.1)
        for click in self.inventory_clicks_list:
            click.position = [click.position.x + x + 0.24, click.position.y, click.position.z]
            click.on_mouse_enter = Func(Inventory.mouse_hover_invslot, self, [click.position.x,click.position.y,click.position.z])

            click.enable()
        for i in self.children:
            i.enable()

        for bgs in self.nums_bg_list:
            bgs.fade_in(value=1, duration=0.3, delay=0.02)

    def hide_inventory(self):
        self.visible = False
        self.pause_menu.filters.setBlurSharpen(amount=1)
        self.background.fade_out(value=0, duration=0.3, delay=0.02)
        for item in self.children:
            item.fade_out(value=0, duration=0.3, delay=0.02)
            invoke(Inventory.hide_items_delay, self, item, delay = 0.5)
        for click in self.inventory_clicks_list:
            click.disable()
        self.highlighted_tile.fade_out(value=0, duration=0.3, delay=0.02)
        self.highlight_click_tile.fade_out(value=0, duration=0.3, delay=0.02)
        for i in self.children:
            i.disable()

        for bgs in self.nums_bg_list:
            bgs.fade_out(value=0, duration=0.3, delay=0.02)

    def add_item(self, _item_, category, item_amount, tradeable):
        current_item_ids = []
        for i in self.children:
            current_item_ids.append(i.tag[0])

        if _item_ not in current_item_ids:
            self.append(item = _item_, tagged = category, amount = item_amount, tradeable = tradeable)
            print('Még nem létezett, szóval létrehoztam')

        else:
            for child in self.children:
                if child.tag[0] == _item_:
                    child.tag[2] += item_amount
                    child.children[1].text = child.tag[2]
                    print('Már létezik')








########################################################################################################################
# BUILDER MODE #

class BuilderModeHud():
    def __init__(self):
        self.grid = Entity(texture = grid, model = 'quad', position = (0,0,-0.3), scale = (15, 15, 0), alpha = 0)

    # ------------------------------------------------------------------------------------------------------------------

    def open_builder_mode(self):
        self.grid.fade_in(value = 1, duration = 0.2, delay = 0.1)

    def close_builder_mode(self):
        self.grid.fade_out(value = 0, duration = 0.2, delay = 0.1)

    # ------------------------------------------------------------------------------------------------------------------
    # DRAW GRIDS

    def update_grid(self, x, y):
        self.grid.position = (x + 0.5, y + 0.5)


















