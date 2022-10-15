from ursina import *from ursina.raycaster import raycastfrom functions import *from random import *app = Ursina()#EditorCamera()#create_net()#background = Entity(model = 'cube', collider = 'box', scale = (1000,1000,0), color = color.dark_gray, position = (0,0,0.1))def collison_hit():    pass'''class Grid:    def __init__(self, pygame):        self.grid = [[0 for x in range(8)] for y in range(8)]'''class Player(Entity):    def update(self):        global movespeed        right_hit = right.intersects(debug=False, ignore=(right, left, up, down))        left_hit = left.intersects(debug=False, ignore=(right, left, up, down))        up_hit = up.intersects(debug=False, ignore=(right, left, up, down))        down_hit = down.intersects(debug=False, ignore=(right, left, up, down))        if shoot == False:            if held_keys['shift']:                movespeed = 4            else:                movespeed = 2.5        if right_hit.hit == False:            for parts in player_parts:                parts.x += held_keys['d'] * movespeed * time.dt            player.x += held_keys['d'] * movespeed * time.dt        else:            collison_hit()        if left_hit.hit == False:            for parts in player_parts:                parts.x -= held_keys['a'] * movespeed * time.dt            player.x -= held_keys['a'] * movespeed * time.dt        else:            collison_hit()        if up_hit.hit == False:            for parts in player_parts:                parts.y += held_keys['w'] * movespeed * time.dt            player.y += held_keys['w'] * movespeed * time.dt        else:            collison_hit()        if down_hit.hit == False:            for parts in player_parts:                parts.y -= held_keys['s'] * movespeed * time.dt            player.y -= held_keys['s'] * movespeed * time.dt        else:            collison_hit()class Enemy(Entity):    def __init__(self, x, y, hp, list, let_shoot, let_move, **kwargs):        super().__init__(self, **kwargs)        self.x = x        self.y = y        self.model = 'cube'        self.color = color.red        self.scale = (1, 1, 0)        self.position = (self.x, self.y, 0)        self.rotation = (0, 0, 0)        self.tag = 'enemy'        self.collider = 'box'        ##################################################x        self.list = list # a lista, amiben mozoghat        self.current_move = 0 # a jelenlegi állása a listában        self.hp = hp        self.shot_bullet = [] # tartalmazza a kilőtt golyókat        self.shoot_delay = 1 # sec / ennyi időnként enged lőni (ez random)        self.ammo = 25        self.loaded_ammo = 8        self.now_you_see_me = False        self.let_shoot = let_shoot        self.let_move = let_move########################################################################################################################wawe_movements = [ [13,2,0],[15,2,0],[15,2,0] ,[16,2,0],[17,2,0],[17,3,0],[18,3,0],[18,4,0],[21,4,0],[15,4,0] ], \                 [ [-13,-2,0],[-14,-2,0],[-15,-2,0],[-16,-2,0],[-17,-2,0],[-17,-3,0],[-18,-3,0],[-18,-4,0],[-19,-5,0] ], \                 [ [10,1,0] , [8,2,0] , [12,4,0]]test_movement = [[0,0,0] , [0,2,0], [8,2,0]]#               x   y  hp  | move-list |let_shoot|let_moveenemy01 = Enemy(2.3, 0, 50, test_movement, True, True, )'''enemy02 = Enemy(5,-2,50,  wawe_movements[0], True, True, )enemy03 = Enemy(9,-2,50,  wawe_movements[2], True, True, )enemy04 = Enemy(12,-2,50, wawe_movements[1], True, True, )enemy05 = Enemy(15,-2,50, wawe_movements[0], True, True, )enemy06 = Enemy(18,-2,50, wawe_movements[0], True, True, )enemy07 = Enemy(20,-2,50, wawe_movements[1], True, True, )enemy08 = Enemy(22,-2,50, wawe_movements[2], True, True, )enemy09 = Enemy(2.3, 0,50, wawe_movements[2], True, True, )enemy10 = Enemy(50,-2,50,  wawe_movements[1], True, True, )enemy11 = Enemy(90,-2,50,  wawe_movements[0], True, True, )enemy12 = Enemy(30,-2,50, wawe_movements[1], True, True, )enemy13 = Enemy(40,-2,50, wawe_movements[0], True, True, )enemy14 = Enemy(23,-2,50, wawe_movements[0], True, True, )enemy15 = Enemy(29,-2,50, wawe_movements[1], True, True, )enemy16 = Enemy(70,-2,50, wawe_movements[2], True, True, )enemy17 = Enemy(50, 0, 50, wawe_movements[2], True, True, )enemy18 = Enemy(5,-2,50,  wawe_movements[1], True, True, )enemy19 = Enemy(9,-2,50,  wawe_movements[0], True, True, )enemy20 = Enemy(120,-2,50, wawe_movements[1], True, True, )enemy21 = Enemy(150,-20,50, wawe_movements[0], True, True, )enemy22 = Enemy(180,-20,50, wawe_movements[0], True, True, )enemy23 = Enemy(200,-2,50, wawe_movements[1], True, True, )enemy24 = Enemy(220,-20,50, wawe_movements[2], True, True, )'''enemies = [enemy01]#, enemy02, enemy03, enemy04, enemy05, enemy06, enemy07, enemy08, enemy09, enemy10, enemy11, enemy12, enemy13, enemy14, enemy15, enemy16, enemy17, enemy18, enemy19, enemy20, enemy21, enemy22, enemy23, enemy24]################################################################################################################################################################################################################################################full_ammo = 500 # bulletrevolver_ammo = 10 # bulletrevolver_shoot_speed = 0.2 # secpull_up = Trueshoot = Falsedef pull_up_delay():    global pull_up    if pull_up == False:        pull_up = Truedef enemy_shot():    try:        #ray.entity.disable()        del enemies[enemies.index(ray.entity)]        destroy(ray.entity)    except:        print('ERROR #1 - enemy_shot : NoneType object has no attribute: disable()')def input(key):    global pull_up, revolver_ammo, full_ammo, bullet, ray    if key == 'left mouse down':        if pull_up == True and revolver_ammo > 0:            x, y, z = mouse.position            real_pos = player.position + (camera.fov * x, camera.fov * y, 0)            if shoot == True: # Ha a karakter céloz, mikozbe lő                direction = [real_pos[0] - player.x,                             real_pos[1] - player.y, 0]            if shoot == False: # Ha a karakter nem céloz - eredmény hogy nagyobb a szóras                direction = [(real_pos[0] - player.x) + (randint(-500, 500) / 100),                             (real_pos[1] - player.y) + (randint(-500, 500) / 100), 0]            duration = 0.03 * (distance(player.position + [20 * p for p in direction], player.world_position))            bullet = Entity(parent = scene, model = 'sphere', collider = 'box', color = color.black, position = player.position, tag ='projectile', scale = (0.2, 0.2, 0.05))            bullet.animate_position(player.position + [20 * p for p in direction], duration = duration, curve = curve.linear)            invoke(destroy, bullet, delay = 1)            ray = raycast(player.position, direction, distance = 50, ignore = (player, bullet, right, left, up, down), debug = True)            if ray.hit:                if ray.entity.tag == 'building': # ha a golyó 'building' taggal ellátott objectet ér                    destroy(bullet, delay = ray.distance * 0.035)                if ray.entity.tag == 'enemy': # ha a golyó enemy-t talál el.                    invoke(enemy_shot, delay = ray.distance * 0.035)                    destroy(bullet, delay=ray.distance * 0.035)            pull_up = False            revolver_ammo -= 1            invoke(pull_up_delay, delay = revolver_shoot_speed)            #print('\nra:',revolver_ammo)    if key == 'r': # reload        for i in range(10 - revolver_ammo):            if full_ammo > 0:                full_ammo -= 1                revolver_ammo += 1player = Player(model='plane', color = color.orange, scale = (1, 1, -1), position = (0, 0.5, 0), rotation = (90, 0, 0), tag ='player')########################################################################################################################prev_pos = player.world_positiontwo_sec_delay = 0tester_bullet_list = []#\1x/s\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\def slow_check():    pass    invoke(slow_check, delay = 0.5)slow_check()##########################################################################################################def update():    global shoot, movespeed, duration, test_bullet, ebullet_list, tester_bullet_list    #[]----------------------------------------------------------------------------------------------------------------[]    for enemy in enemies:        if enemy.let_move == True:            enemy.look_at_2d(Vec3(enemy.list[enemy.current_move][0],enemy.list[enemy.current_move][1],enemy.list[enemy.current_move][2]))            if distance(enemy, player) >= 2:                if enemy.current_move != len(enemy.list): # amig a current_move nem egyenlő a lista hosszaval                    enemy.position += enemy.up * 0.02 # mozgatas                    if enemy.current_move != len(enemy.list) - 1:                        if round(enemy.position.x, 1) == round(float(enemy.list[enemy.current_move][0]),1): # ellenorzi hogy elerte e a poziciot.                            if round(enemy.position.y, 1) == round(float(enemy.list[enemy.current_move][1]),1):                                enemy.current_move += 1 # tovább lép a következő pontra.            # -------------------------------------------------------------------------------- #            else:                pass # print('közel')        # az ellenségek lövése és köztes akadályok ellenőrzése #####################################        if enemy.let_shoot == True: # ha az adott enemy számára a lövés engedélyezve van.            if distance((enemy.x,0,0), (player.x,0,0)) <= 17.5 and distance((0,enemy.y,0), (0,player.y,0)) <= 11:  # lőtávolság                obstacle_test = raycast(enemy.world_position,                                        direction = player.world_position - enemy.world_position,                                        distance = distance(player, enemy), traverse_target = scene, ignore = [enemy], debug = True)                if obstacle_test.hit:                    for obstacle in obstacle_test.entities:                        try:                            if obstacle.tag == 'building':                                enemy.now_you_see_me = False                            else:                                enemy.now_you_see_me = True                        except: pass # ha esetleg valaminek amin átmegy a ray - nincs tag-je.            if enemy.now_you_see_me == True: # ha az enemy látja a játékost.                self.shot_bullet.append(Entity(parent = scene, model = 'sphere', collider = 'box', color = color.red, position = enemy.position, tag = 'enemy_bullet', scale = (0.2, 0.2, 0.05)))    # []-------------------------------------------------------------------------[]    if held_keys['right mouse']:        shoot = True        movespeed = 1    else:        shoot = False######################################################################################################################### [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]camera.add_script(SmoothFollow(target = player, offset=[0, 1, -50], speed = 4))right = Entity(model='plane', scale=(0.1, 1, -1), position = (0.5, 0.5, 0), color = color.red, rotation = (90,0,0), collider='box', tag = 'collision', visible = False)left = Entity(model='plane', scale=(0.1, 1, -1), position = (-0.5, 0.5, 0), color = color.brown, rotation = (90,0,0), collider='box', tag = 'collision', visible = False)up = Entity(model='plane', scale=(1, 1, -0.1), position = (0, 1, 0), color = color.azure, rotation = (90,0,0), collider='box', tag = 'collision', visible = False)down = Entity(model='plane', scale=(1, 1, -0.1), position = (0, 0, 0), color = color.pink, rotation = (90,0,0), collider='box', tag = 'collision', visible = False)player_parts = [right, left, up, down]object1 = Entity(model='cube', collider='mesh', scale=(3,5,0), color = color.gray, position = (-7,2,0), tag = 'building')'''object = Entity(model='cube', collider='mesh', scale=(1,1,0), color = color.gray, x = -3, y = 3.6, tag = 'building')object = Entity(model='cube', collider='mesh', scale=(1,1,0), color = color.gray, x = -2.3, y = 0, tag = 'building')object = Entity(model='cube', collider='mesh', scale=(1,4,0), color = color.gray, x = -2, y = 0, tag = 'building')object = Entity(model='cube', collider='mesh', scale=(1,2,0), color = color.gray, x = -3, y = -1, tag = 'building')object = Entity(model='cube', collider='mesh', scale=(5,5,0), color = color.gray, x = 8, y = 2, tag = 'building')tower = Entity(model='cube', collider='mesh', scale=(2,2,0), color = color.violet, x = -8, y = -5, tag = 'tower')tower = Entity(model='cube', collider='mesh', scale=(2,2,0), color = color.violet, x = -10, y = 3, tag = 'tower')tower = Entity(model='cube', collider='mesh', scale=(2,2,0), color = color.violet, x =  2, y = 8, tag = 'tower')'''objects_list = [object1]app.run()