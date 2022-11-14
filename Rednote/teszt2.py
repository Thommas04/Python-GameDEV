from ursina import *from ursina.raycaster import raycastfrom functions import *from random import *from pathfinding.core.diagonal_movement import DiagonalMovementfrom pathfinding.core.grid import Gridfrom pathfinding.finder.a_star import AStarFinderapp = Ursina()#EditorCamera()#create_net()#background = Entity(model = 'cube', collider = 'box', scale = (1000,1000,0), color = color.dark_gray, position = (0,0,0.1))# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] ## 2D MATRIX# minden elemének eleme egy lista, amelynek#               - első eleme : / szabad e az adott terület [ True / False ]#               - második eleme: / blokkok neve, melyhez tulajdonságokat társítunk. [ grass, path, stone, wood ]#               - harmadik eleme: /class Matrix:    def __init__(self, size_x, size_y):        self.matrix = [[1 for x in range(size_x)] for y in range(size_y)]    def get_value(self, state, x, y): # visszaadja az adott terület értékét        return self.grid[y][x][state]    def set_value(self, state, x, y, value): # adott területre értéket állít        self.grid[y][x][state] = value    def g_print(self): # printeli a mátrixot        for x in self.grid:            print(f'{x}')moveable_area = Matrix(size_x = 200, size_y = 200)# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] #def collison_hit():    passclass Player(Entity):    def update(self):        global movespeed        right_hit = right.intersects(debug=False, ignore=(right, left, up, down))        left_hit = left.intersects(debug=False, ignore=(right, left, up, down))        up_hit = up.intersects(debug=False, ignore=(right, left, up, down))        down_hit = down.intersects(debug=False, ignore=(right, left, up, down))        if shoot == False:            if held_keys['shift']:                movespeed = 4            else:                movespeed = 2.5        if right_hit.hit == False:            for parts in player_parts:                parts.x += held_keys['d'] * movespeed * time.dt            player.x += held_keys['d'] * movespeed * time.dt        else: collison_hit()        if left_hit.hit == False:            for parts in player_parts:                parts.x -= held_keys['a'] * movespeed * time.dt            player.x -= held_keys['a'] * movespeed * time.dt        else: collison_hit()        if up_hit.hit == False:            for parts in player_parts:                parts.y += held_keys['w'] * movespeed * time.dt            player.y += held_keys['w'] * movespeed * time.dt        else: collison_hit()        if down_hit.hit == False:            for parts in player_parts:                parts.y -= held_keys['s'] * movespeed * time.dt            player.y -= held_keys['s'] * movespeed * time.dt        else: collison_hit()######################################################################################################################## [ Place Class ] ###################################################################################################class Place(Entity):    def __init__(self, tag, x, y, hp, let_shoot, target, unbreakable, brokable_with, **kwargs):        super().__init__(self, **kwargs)        self.global_time = 0        self.last_time = 0        self.x = x        self.y = y        self.model = 'cube'        self.color = color.violet        self.position = (self.x, self.y, 0)        self.rotation = (0, 0, 0)        self.tag = tag        self.collider = 'mesh'        self.scale = (3, 3, 0)        self.hp = hp        self.target = target # ellenség vagy a játékos a cél        self.let_shoot = let_shoot # lőhet-e, ez tornyok esetében jelentős        self.unbreakable = unbreakable # törhetetlen-e vagy sem - True / False        self.brokable_with = brokable_with # kitörhető valamilyen tárggyal a kézben, ez egy list is lehet.        self.shoot_cooldown = True        self.tower_bullets = []  # tartalmazza a kilőtt golyókat    def update(self):        if self.let_shoot == True:            self.global_time += time.dt            if self.global_time - self.last_time > (randint(100, 150) / 100):  # random időközönként ad engedélyt                self.last_time = self.global_time                self.shoot_cooldown = True            for enemy in enemies:                if enemy.alive == True:                    if distance([enemy.x, enemy.y, 0],[self.x, self.y, 0]) <= 15:                        if self.shoot_cooldown == True:                            tower_bullet = Entity(parent = scene, model = 'sphere',                                                  color = color.red, position = self.world_position, tag = 'tower_bullet',                                                  scale = (0.2, 0.2, 0.05))                            self.tower_bullets.append(tower_bullet)                            if self.target == 'enemy':                                tower_bullet.look_at_2d(Vec3(enemy.world_position))                                print(len(enemies))                        self.shoot_cooldown = False                #[] -----------------\\\///-------[]                for bullet in self.tower_bullets:                    bullet.world_position += bullet.up * 35 * time.dt  # a hányados takarja a sebességét a golyónak                    if enemy.alive == True:                        if distance(enemy, bullet) <= 1:                            self.tower_bullets.remove(bullet)                            destroy(bullet)                            enemy.color = color.black                            enemy.alive = False                            print('torony ellenségett lőtt')                    elif distance(enemy, bullet) > 20:                        destroy(bullet)                        self.tower_bullets.remove(bullet)######################################################################################################################## [ SPAWNER Class ] ###################################################################################################class Spawner(Entity): # includes enemies ; npc-s ; towers ;    def __init__(self, tag, x, y, hp, list, let_shoot, let_move, invincible, **kwargs):        super().__init__(self, **kwargs)        self.global_time = 0  #        self.last_time = 0        self.global_time_reload = 0  #        self.last_time_reload = 0        self.x = x        self.y = y        self.model = 'cube'        self.color = color.red        self.position = (self.x, self.y, 0)        self.rotation = (0, 0, 0)        self.tag = tag        self.collider = 'mesh'        ##################################################x        self.list = list # a lista, amiben mozoghat        self.current_move = 0 # a jelenlegi állása a listában        self.invincible = invincible        self.alive = True        self.hp = hp        self.reload_enable = False # engedély újratöltésre - True ha üres a tár.        self.reloaded = False # Újratöltés befejezve. < késleltetve >        self.shot_bullet = [] # tartalmazza a kilőtt golyókat        self.shoot_directed = False  # True, ha a golyó kapott irányt.        self.shoot_delayed = False        self.full_ammo = 11        self.loaded_ammo = 8        self.now_you_see_me = False # True ha a játékos a látóterében van, és nem takarja semmilyen fal.        self.let_shoot = let_shoot        self.scale = (1, 1, 0)        self.let_move = let_move    def update(self):        self.global_time += time.dt        if self.global_time - self.last_time > (randint(100,200) / 100):  # random időközönként ad engedélyt            self.last_time = self.global_time            self.shoot_delayed = True        if self.full_ammo != 0:            if self.reload_enable == True:                self.global_time_reload += time.dt                self.reload_enable = False                if self.global_time_reload - self.last_time_reload > 3:  # random időközönként ad engedélyt                    self.last_time_reload = self.global_time_reload                    self.shoot_delayed_reload = True                    print('helo')                    self.reloaded = True#____________________________________________________________________________________________________________________## [ CONSTANTS ] ######################################################################################################wawe_movements = [ [13,2,0],[15,2,2],[15,2,0] ,[16,2,0],[17,2,5],[17,3,0],[18,3,10],[18,4,0],[21,4,0],[15,4,0] ], \                 [ [-13,-2,0],[-14,-2,0],[-15,-2,0],[-16,-2,0],[-17,-2,0],[-17,-3,0],[-18,-3,0],[-18,-4,0],[-19,-5,0] ], \                 [ [10,1,0] , [8,2,0] , [12,4,0]]test_movement = [[0,0,0] , [0,2,0], [8,6,0], [10,5,0]]#                   tag   x   y  hp  | move-list  |  let_shoot|let_move| invincibleenemy01 = Spawner('enemy',1, 2, 50, test_movement    , True, True, False )enemy02 = Spawner('enemy',5, -2, 50, test_movement, True , True, False )enemy03 = Spawner('enemy',9, -2, 50, wawe_movements[2], True , True, False )enemy04 = Spawner('enemy',12, -2, 50, wawe_movements[1], True, True, False )enemy05 = Spawner('enemy',15, -2, 50, wawe_movements[0], True, True, False )enemy06 = Spawner('enemy',18, -2, 50, wawe_movements[0], True, True, False )enemy07 = Spawner('enemy',20, -2, 50, wawe_movements[1], True, True, False )enemy08 = Spawner('enemy',22, -2, 50, wawe_movements[2], True, True, False )enemy09 = Spawner('enemy',2.3, 0, 50, wawe_movements[2], True, True, False )enemy10 = Spawner('enemy',50, -2, 50, wawe_movements[1], True, True, False )enemy11 = Spawner('enemy',90, -2, 50, wawe_movements[0], True, True, False )enemy12 = Spawner('enemy',30, -2, 50, wawe_movements[1], True, True, False )enemy13 = Spawner('enemy',40, -2, 50, wawe_movements[0], True, True, False )enemy14 = Spawner('enemy',23, -2, 50, wawe_movements[0], True, True, False )enemy15 = Spawner('enemy',29, -2, 50, wawe_movements[1], True, True, False )enemy16 = Spawner('enemy',70, -2, 50, wawe_movements[2], True, True, False )enemy17 = Spawner('enemy',50,  0, 50, wawe_movements[2], True, True, False )enemy18 = Spawner('enemy',5 , -2, 50, wawe_movements[1], True, True, False )enemy19 = Spawner('enemy',9 , -2, 50, wawe_movements[0], True, True, False )enemy20 = Spawner('enemy',12, -2, 50, wawe_movements[1], True, True, False )enemy21 = Spawner('enemy',15, -20, 50,wawe_movements[0], True, True, False )enemy22 = Spawner('enemy',18, -20, 50,wawe_movements[0], True, True, False )enemy23 = Spawner('enemy',20, -2, 50, wawe_movements[1], True, True, False )enemy24 = Spawner('enemy',22, -20, 50,wawe_movements[2], True, True, False )enemies = [enemy01, enemy02, enemy03, enemy04, enemy05, enemy06, enemy07, enemy08, enemy09, enemy10, enemy11, enemy12, enemy13, enemy14, enemy15, enemy16, enemy17, enemy18, enemy19, enemy20, enemy21, enemy22, enemy23, enemy24]tower01 = Place(tag = 'tower', x = 10, y = 10, hp = 100, let_shoot = True, target = 'enemy', unbreakable = False, brokable_with = ['bullet','explosive'])tower02 = Place(tag = 'tower', x = 5, y = 8, hp = 100, let_shoot = True, target = 'enemy', unbreakable = False, brokable_with = ['bullet','explosive'])tower03 = Place(tag = 'tower', x = 13, y = -3, hp = 100, let_shoot = True, target = 'enemy', unbreakable = False, brokable_with = ['bullet','explosive'])################################################################################################################################################################################################################################################full_ammo = 500 # bulletrevolver_ammo = 10 # bulletrevolver_shoot_speed = 0.2 # secpull_up = Trueshoot = Falsedef pull_up_delay():    global pull_up    if pull_up == False:        pull_up = True# [] ------------------------------------------------------------------------------------------------------------------[]def enemy_shot():    #ray.entity.disable()    try:        if not ray.entity.invincible:            ray.entity.alive = False            ray.entity.color = color.black            #del enemies[enemies.index(ray.entity)] #törli az adott entityt a listából    except: pass# [] ------------------------------------------------------------------------------------------------------------------[]def player_got_shot():    print('meglőttek')def relocate(entity, x, y): # A* movement    grid = Grid(matrix=moveable_area.matrix)    start = grid.node(int(entity.x), int(entity.y))    end = grid.node(x, y)    finder = AStarFinder()    path, runs = finder.find_path(start, end, grid)    list_path = []    for i in range(len(path)):        list_path.append([path[i][0], path[i][1],0])    return list_path# [] ------------------------------------------------------------------------------------------------------------------[]def input(key):    if key == 'left mouse down':        x, y, z = mouse.position        #print(relocate(enemy01, 50, 10))    global pull_up, revolver_ammo, full_ammo, bullet, ray    if key == 'left mouse down':        if pull_up == True and revolver_ammo > 0:            x, y, z = mouse.position            real_pos = player.position + (camera.fov * x, camera.fov * y, 0)            if shoot == True: # Ha a karakter céloz, mikozbe lő                direction = [real_pos[0] - player.x,                                real_pos[1] - player.y, 0]            if shoot == False: # Ha a karakter nem céloz - eredmény hogy nagyobb a szóras                direction = [(real_pos[0] - player.x) + (randint(-500, 500) / 100),                                (real_pos[1] - player.y) + (randint(-500, 500) / 100), 0]            duration = 0.03 * (distance(player.position + [20 * p for p in direction], player.world_position))            bullet = Entity(parent = scene, model = 'sphere', collider = 'box', color = color.black, position = player.position, tag ='projectile', scale = (0.2, 0.2, 0.05))            bullet.animate_position(player.position + [20 * p for p in direction], duration = duration, curve = curve.linear)            invoke(destroy, bullet, delay = 1)            ray = raycast(player.position, direction, distance = 50, ignore = (player, bullet, right, left, up, down), debug = True)            if ray.hit:                if ray.entity.tag == 'building': # ha a golyó 'building' taggal ellátott objectet ér                    destroy(bullet, delay = ray.distance * 0.035)                if ray.entity.tag == 'enemy': # ha a golyó enemy-t talál el.                    invoke(enemy_shot, delay = ray.distance * 0.035)                    destroy(bullet, delay=ray.distance * 0.035)            pull_up = False            revolver_ammo -= 1            invoke(pull_up_delay, delay = revolver_shoot_speed)            #print('\nra:',revolver_ammo)    if key == 'r': # reload        for i in range(10 - revolver_ammo):            if full_ammo > 0:                full_ammo -= 1                revolver_ammo += 1 # hangot lejátsza invoke-kal késleltetve, hozzáadott idővel.player = Player(model='plane', color = color.orange, scale = (1, 1, -1), position = (0, 0.5, 0), rotation = (90, 0, 0), tag ='player')player.alpha = 0.1##################################################################################################################################################################################################################################def update():    global shoot, movespeed, duration, test_bullet, ebullet_list, tester_bullet_list    #[]----------------------------------------------------------------------------------------------------------------[]    for enemy in enemies:        if enemy.alive:            if enemy.let_move == True:                enemy.look_at_2d(Vec3(enemy.list[enemy.current_move][0],enemy.list[enemy.current_move][1],enemy.list[enemy.current_move][2]))                if distance(enemy, player) >= 2:                    if enemy.current_move != len(enemy.list): # amíg a current_move nem egyenlő a lista hosszával                        enemy.position += enemy.up * 0.02 # mozgatás                        if enemy.current_move != len(enemy.list) - 1:                            if round(enemy.position.x, 1) == round(float(enemy.list[enemy.current_move][0]),1): # ellenőrzi hogy elérte e a pozíciót.                                if round(enemy.position.y, 1) == round(float(enemy.list[enemy.current_move][1]),1):                                    enemy.current_move += 1 # tovább lép a következő pontra.          #[]------------------------------------------------------------------------------------------------------------[]            # az ellenségek lövése és köztes akadályok ellenőrzése #####################################            if enemy.let_shoot == True: # ha az adott enemy számára a lövés engedélyezve van.                if distance((enemy.x,0,0), (player.x,0,0)) <= 17.5 and distance((0,enemy.y,0), (0,player.y,0)) <= 11:  # lőtávolság                    obstacle_test = raycast(enemy.world_position,                                            direction = player.world_position - enemy.world_position,                                            distance = distance(player, enemy), traverse_target = scene, ignore = [enemy], debug = False)                    if obstacle_test.hit: # felsorolt elemeken keresztül nem lőhet rád az enemy                        if obstacle_test.entity.tag == 'enemy' or obstacle_test.entity.tag == 'building' or obstacle_test.entity.tag == 'tower':                            enemy.now_you_see_me = False                        else:                            enemy.now_you_see_me = True                else:                    enemy.now_you_see_me = False                if enemy.now_you_see_me == True: # ha az enemy látja a játékost.                    if enemy.loaded_ammo != 0:                        if enemy.shoot_delayed == True:                            enemy.shoot_delayed = False                            enemy_bullet = Entity(parent=scene, model='sphere', collider='box',                                                  color=color.red, position = enemy.world_position, tag = 'enemy_bullet', scale = (0.2, 0.2, 0.05))                            enemy_bullet.look_at_2d(Vec3(player.world_position       ))                            enemy.shot_bullet.append(enemy_bullet)                            enemy.loaded_ammo -= 1                            print(enemy.loaded_ammo)                    if enemy.loaded_ammo == 0:                        enemy.reload_enable = True # Várnia kell 3 másodpercet míg újratölt                        if enemy.full_ammo != 0:                            a = 8                            if enemy.full_ammo < 8: # ha kevesebb mint 8 tölténye maradt, akkor csak annyit tölthessen vissza.                                a = enemy.full_ammo                            if enemy.reloaded == True:                                for i in range(a - enemy.loaded_ammo):                                    if enemy.full_ammo > 0:                                        enemy.full_ammo -= 1                                        enemy.loaded_ammo += 1  # hangot lejátsza invoke-kal késleltetve, hozzáadott idővel.                                print('ammo:',enemy.full_ammo)        #[]--------------------------------------------------------------------------------------------------------[]        for bullet in enemy.shot_bullet:            bullet.world_position += bullet.up * 150 * time.dt  # a hányados takarja a sebességét a golyónak            if distance(player, bullet) <= 1:                enemy.shot_bullet.remove(bullet)                player_got_shot()                destroy(bullet)            elif distance(player, bullet) > 20:                enemy.shot_bullet.remove(bullet)                destroy(bullet)    #[]-------------------------------------------------------------------------[]    if held_keys['right mouse']:        shoot = True        movespeed = 1    else:        shoot = False######################################################################################################################### [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]camera.add_script(SmoothFollow(target = player, offset=[0, 1, -50], speed = 4))right = Entity(model='plane', scale=(0.1, 1, -1), position = (0.5, 0.5, 0), color = color.red, rotation = (90,0,0), collider='box', tag = 'collision', visible = False)left = Entity(model='plane', scale=(0.1, 1, -1), position = (-0.5, 0.5, 0), color = color.brown, rotation = (90,0,0), collider='box', tag = 'collision', visible = False)up = Entity(model='plane', scale=(1, 1, -0.1), position = (0, 1, 0), color = color.azure, rotation = (90,0,0), collider='box', tag = 'collision', visible = False)down = Entity(model='plane', scale=(1, 1, -0.1), position = (0, 0, 0), color = color.pink, rotation = (90,0,0), collider='box', tag = 'collision', visible = False)player_parts = [right, left, up, down]object1 = Entity(model='cube', collider='mesh', scale=(3,5,0), color = color.gray, position = (-7,2,0), tag = 'building')object = Entity(model='cube', collider='mesh', scale=(1,1,0), color = color.gray, x = -3, y = 3.6, tag = 'building')object = Entity(model='cube', collider='mesh', scale=(1,1,0), color = color.gray, x = -2.3, y = 0, tag = 'building')object = Entity(model='cube', collider='mesh', scale=(1,4,0), color = color.gray, x = -2, y = 0, tag = 'building')object = Entity(model='cube', collider='mesh', scale=(1,2,0), color = color.gray, x = -3, y = -1, tag = 'building')object = Entity(model='cube', collider='mesh', scale=(5,5,0), color = color.gray, x = 8, y = 2, tag = 'building')objects_list = [object1]app.run()