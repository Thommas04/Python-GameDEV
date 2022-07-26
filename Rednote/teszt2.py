from ursina import *
from ursina.raycaster import raycast
from functions import *
from random import *

app = Ursina()
#EditorCamera()
create_net()

#background = Entity(model = 'cube', collider = 'box', scale = (1000,1000,0), color = color.dark_gray, position = (0,0,0.1))

def collison_hit():
    pass

class Player(Entity):
    def update(self):
        global movespeed
        right_hit = right.intersects(debug = False, ignore = (right, left, up, down))
        left_hit = left.intersects(debug = False, ignore = (right, left, up, down))
        up_hit = up.intersects(debug = False, ignore = (right, left, up, down))
        down_hit = down.intersects(debug = False, ignore = (right, left, up, down))

        if shoot == False:
            if held_keys['shift']:
                movespeed = 4
            else:
                movespeed = 2.5

        if right_hit.hit == False:
            right.x += held_keys['d'] * movespeed * time.dt
            left.x += held_keys['d'] * movespeed * time.dt
            up.x += held_keys['d'] * movespeed * time.dt
            down.x += held_keys['d'] * movespeed * time.dt
            self.x += held_keys['d'] * movespeed * time.dt
        else:
            collison_hit()

        if left_hit.hit == False:
            right.x -= held_keys['a'] * movespeed * time.dt
            left.x -= held_keys['a'] * movespeed * time.dt
            up.x -= held_keys['a'] * movespeed * time.dt
            down.x -= held_keys['a'] * movespeed * time.dt
            self.x -= held_keys['a'] * movespeed * time.dt
        else:
            collison_hit()

        if up_hit.hit == False:
            right.y += held_keys['w'] * movespeed * time.dt
            left.y += held_keys['w'] * movespeed * time.dt
            up.y += held_keys['w'] * movespeed * time.dt
            down.y += held_keys['w'] * movespeed * time.dt
            self.y += held_keys['w'] * movespeed * time.dt
        else:
            collison_hit()

        if down_hit.hit == False:
            right.y -= held_keys['s'] * movespeed * time.dt
            left.y -= held_keys['s'] * movespeed * time.dt
            up.y -= held_keys['s'] * movespeed * time.dt
            down.y -= held_keys['s'] * movespeed * time.dt
            self.y -= held_keys['s'] * movespeed * time.dt
        else:
            collison_hit()

class Enemy(Entity):
    def __init__(self, x, y, hp, list, tag, **kwargs):
        super().__init__(self, **kwargs)
        self.x = x
        self.y = y
        self.hp = hp
        self.current_move = 0
        self.list = list
        self.model = 'cube'
        self.color = color.red
        self.scale = (1, 0, 1)
        self.position = (self.x, self.y, 0)
        self.rotation = (90, 0, 0)
        self.tag = 'enemy'
        self.collider = 'box'

        self.move_scale_x = []
        self.move_scale_y = []
        self.moves_list = []

        self.list.insert(0, [self.position.x,self.position.y, self.position.z]) # a listaba helyezi az enemy pillanatnyi poziciojat

        for i in range(1, len(self.list)): # 1-tol kezdodoen lefut annyiszor amennyi elem van az objektum listajaban.
            #print(self.list[iance])
            range_x = int(distance((self.list[i][0],0,0), (self.list[i - 1][0],0,0)) * 10) # tavolsag ket pont kozt a tengelyen x10.
            range_y = int(distance((0,self.list[i][1],0), (0,self.list[i - 1][1],0)) * 10)
            #print('range:', range_y)

            # [x]------------------------------------------------------------------[]

            counter_y = 0
            for scale_x in range(range_x + 1): # a tavot egysegekre bontva lefuttatja 10x
                rx = [round(self.list[i - 1][0] + (0.1 * scale_x), 2), 0, 0] # ha x ereteke nagyobb, ugy o a master.
                self.move_scale_x.append(rx)

                try:
                    y_locker = round(range_x / range_y)
                except ZeroDivisionError:
                    y_locker = 0

                if counter_y == y_locker: # az y e'rte'ke ke'sleltetve kap e'rteket, hogy ara'nyos legyen az x-hez ke'pest.
                    ry = [0, round(self.list[i - 1][1] + (0.1 * scale_x), 2), 0]
                    self.move_scale_y.append(ry)
                    counter_y = 0
                else:
                    counter_y += 1
                    if len(self.move_scale_y) <= y_locker:
                        self.move_scale_y.append([0,0,0])
                    else:
                        self.move_scale_y.append(self.move_scale_y[-1])

            # [y]------------------------------------------------------------------[]

        for merge in range(len(self.move_scale_x)):
            self.moves_list.append([self.move_scale_x[merge], self.move_scale_y[merge], 0])

        print(len(self.move_scale_x), self.move_scale_x)
        print(len(self.move_scale_y), self.move_scale_y)

########################################################################################################################

# 0.1 a legkisebb ertek, igy a 10x-es szorzata = 1
# 15/1 = 15
# 15/2 = 7.5
# 15/3 = 5

wawe_movements = [ [13,2,0],[15,2,0],[15,2,0] ,[16,2,0],[17,2,0],[17,3,0],[18,3,0],[18,4,0],[21,4,0],[60,4,0] ], \
                 [ [-13,-2,0],[-14,-2,0],[-15,-2,0],[-16,-2,0],[-17,-2,0],[-17,-3,0],[-18,-3,0],[-18,-4,0],[-19,-5,0] ], \
                 [ [10.6,1,0] , [8,2,0] , [12.9,0.1,0]]

list1 = [[13,2,0],[14,2,0]]
list2 = [3,4,0]

list1.insert(1, ['almaa'])
#print(list1)

enemy1 = Enemy(2.3, 0, 50, wawe_movements[2], 'e1')

#enemy2 = Enemy(5,-2,50,  wawe_movements[1], 'e2')
'''enemy3 = Enemy(9,-2,50,  wawe_movements[0], 'e3')
enemy4 = Enemy(12,-2,50, wawe_movements[1], 'e4')
enemy5 = Enemy(15,-2,50, wawe_movements[0], 'e5')
enemy6 = Enemy(18,-2,50, wawe_movements[0], 'e6')
enemy7 = Enemy(20,-2,50, wawe_movements[1], 'e7')
enemy8 = Enemy(22,-2,50, wawe_movements[2], 'e8')'''

enemies = [enemy1]#, enemy2]#, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8]

########################################################################################################################


########################################################################################################################

full_ammo = 500 # bullet
revolver_ammo = 10 # bullet
revolver_shoot_speed = 0.2 # sec
pull_up = True
shoot = False

def pull_up_delay():
    global pull_up
    if pull_up == False:
        pull_up = True

def enemy_shot():
    try:
        #ray.entity.disable()
        del enemies[enemies.index(ray.entity)]
        destroy(ray.entity)
    except:
        print('ERROR #1 - enemy_shot : NoneType object has no attribute: disable()')

def input(key):
    global pull_up, revolver_ammo, full_ammo, bullet, ray
    if key == 'left mouse down':
        if pull_up == True and revolver_ammo > 0:
            x, y, z = mouse.position
            real_pos = lower_body.position + (camera.fov * x, camera.fov * y, 0)

            if shoot == True: # Ha a karakter celoz, mikozbe lo
                direction = [real_pos[0] - lower_body.x,
                             real_pos[1] - lower_body.y, 0]
            if shoot == False: # Ha a karakter nem celoz - eredmeny hogy nagyobb a szoras
                direction = [(real_pos[0] - lower_body.x) + (randint(-500,500) / 100),
                             (real_pos[1] - lower_body.y) + (randint(-500,500) / 100), 0]

            duration = 0.03 * (distance(lower_body.position + [20 * p for p in direction], lower_body.world_position))
            bullet = Entity(parent = scene, model = 'sphere', collider = 'box', color = color.black, position = lower_body.position, tag = 'projectile', scale = (0.2, 0.2, 0.05))
            bullet.animate_position(lower_body.position + [20 * p for p in direction], duration = duration, curve = curve.linear)
            invoke(destroy, bullet, delay = 1)

            ray = raycast(lower_body.position, direction, distance = 50, ignore = (lower_body, bullet, right, left, up, down), debug = True)
            if ray.hit:
                if ray.entity.tag == 'building': # ha a golyo 'building' taggal ellatott objectet er
                    destroy(bullet, delay = ray.distance * 0.035)

                if ray.entity.tag == 'enemy': # ha a golyo enemy-t talal el.
                    invoke(enemy_shot, delay = ray.distance * 0.035)
                    destroy(bullet, delay=ray.distance * 0.035)

            pull_up = False
            revolver_ammo -= 1
            invoke(pull_up_delay, delay = revolver_shoot_speed)
            #print('\nra:',revolver_ammo)

    if key == 'r': # reload
        for i in range(10 - revolver_ammo):
            if full_ammo > 0:
                full_ammo -= 1
                revolver_ammo += 1

lower_body = Player(model='plane', color = color.orange, scale = (1,1,-1), position = (0,0.5,0), rotation = (90,0,0), tag = 'player')

def move_enemy():
    global duration
    for enemy in enemies:
        if distance(enemy, lower_body) >= 3:
            if enemy.current_move != len(enemy.list):
                target_position = enemy.list[enemy.current_move][0] + (randint(-20, 20) / 100), \
                                  enemy.list[enemy.current_move][1] + (randint(-20, 20) / 100), \
                                  enemy.list[enemy.current_move][2]
                duration = distance(enemy.world_position, target_position) * 0.5
                #print(enemy.tag)

                #print(target_position)
                enemy.animate_position(target_position, duration = duration ,curve=curve.linear)
                if enemy.current_move != len(enemy.list) - 1:
                    enemy.current_move += 1
        else:
            print('kozel')

    invoke(move_enemy, delay = 0.5)


move_enemy()


def update():
    global shoot, movespeed
    if held_keys['right mouse']:
        shoot = True
        movespeed = 1
    else:
        shoot = False

    #ai
'''    for i in enemies:
        enemy_hit = i.intersects(debug = True, ignore = (i,))
        if distance(i, lower_body) > 3 and enemy_hit.hit == False:
            i.x += 0.005'''

        #ray = raycast(i.position, -lower_body.world_position, distance=51, ignore=(),debug=True)

########################################################################################################################
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]


camera.add_script(SmoothFollow(target = lower_body, offset=[0,1,-50], speed=4))

right = Entity(model='plane', scale=(0.1, 1, -1), position = (0.5, 0.5, 0), color = color.red, rotation = (90,0,0), collider='box')
left = Entity(model='plane', scale=(0.1, 1, -1), position = (-0.5, 0.5, 0), color = color.brown, rotation = (90,0,0), collider='box')
up = Entity(model='plane', scale=(1, 1, -0.1), position = (0, 1, 0), color = color.azure, rotation = (90,0,0), collider='box')
down = Entity(model='plane', scale=(1, 1, -0.1), position = (0, 0, 0), color = color.pink, rotation = (90,0,0), collider='box')

object = Entity(model='cube', collider='mesh', scale=(3,5,0), color = color.gray, x = -7, y = 2, tag = 'building')
object = Entity(model='cube', collider='mesh', scale=(1,1,0), color = color.gray, x = -3, y = 3.6, tag = 'building')
object = Entity(model='cube', collider='mesh', scale=(1,1,0), color = color.gray, x = -2.3, y = 0, tag = 'building')
object = Entity(model='cube', collider='mesh', scale=(1,4,0), color = color.gray, x = -2, y = 0, tag = 'building')
object = Entity(model='cube', collider='mesh', scale=(1,2,0), color = color.gray, x = -3, y = -1, tag = 'building')
object = Entity(model='cube', collider='mesh', scale=(5,5,0), color = color.gray, x = 8, y = 2, tag = 'building')

tower = Entity(model='cube', collider='mesh', scale=(2,2,0), color = color.red, x = -8, y = -5, tag = 'tower')
tower = Entity(model='cube', collider='mesh', scale=(2,2,0), color = color.red, x = -10, y = 3, tag = 'tower')
tower = Entity(model='cube', collider='mesh', scale=(2,2,0), color = color.red, x =  2, y = 8, tag = 'tower')

#Artif.enemy_go_to(Tomi2, 5, 8)

app.run()