from ursina import *
from ursina.raycaster import raycast
from functions import *
from random import *

app = Ursina()
#EditorCamera()
#create_net()

#background = Entity(model = 'cube', collider = 'box', scale = (1000,1000,0), color = color.dark_gray, position = (0,0,0.1))
#player_parts = [right, left, up, down]

def collison_hit():
    pass

'''class Grid:
    def __init__(self, pygame):
        self.grid = [[0 for x in range(8)] for y in range(8)]'''

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
        self.scale = (1, 1, 0)
        self.position = (self.x, self.y, 0)
        self.rotation = (0, 0, 0)
        self.tag = 'enemy'
        self.collider = 'box'

        self.move_scale_x = []
        self.move_scale_y = []
        self.moves_list = []

########################################################################################################################

wawe_movements = [ [13,2,0],[15,2,0],[15,2,0] ,[16,2,0],[17,2,0],[17,3,0],[18,3,0],[18,4,0],[21,4,0],[15,4,0] ], \
                 [ [-13,-2,0],[-14,-2,0],[-15,-2,0],[-16,-2,0],[-17,-2,0],[-17,-3,0],[-18,-3,0],[-18,-4,0],[-19,-5,0] ], \
                 [ [10,1,0] , [8,2,0] , [12,4,0]]

enemy1 = Enemy(2.3, 0, 50, wawe_movements[0], 'e1')
enemy2 = Enemy(5,-2,50,  wawe_movements[0], 'e2')
enemy3 = Enemy(9,-2,50,  wawe_movements[0], 'e3')
enemy4 = Enemy(12,-2,50, wawe_movements[1], 'e4')
enemy5 = Enemy(15,-2,50, wawe_movements[0], 'e5')
enemy6 = Enemy(18,-2,50, wawe_movements[0], 'e6')
enemy7 = Enemy(20,-2,50, wawe_movements[1], 'e7')
enemy8 = Enemy(22,-2,50, wawe_movements[2], 'e8')
enemy9 = Enemy(2.3, 0, 50, wawe_movements[2], 'e1')
enemy10 = Enemy(50,-2,50,  wawe_movements[1], 'e2')
enemy11 = Enemy(90,-2,50,  wawe_movements[0], 'e3')
enemy12 = Enemy(30,-2,50, wawe_movements[1], 'e4')
enemy13 = Enemy(40,-2,50, wawe_movements[0], 'e5')
enemy14 = Enemy(23,-2,50, wawe_movements[0], 'e6')
enemy15 = Enemy(29,-2,50, wawe_movements[1], 'e7')
enemy16 = Enemy(70,-2,50, wawe_movements[2], 'e8')
enemy17 = Enemy(50, 0, 50, wawe_movements[2], 'e1')
enemy18 = Enemy(5,-2,50,  wawe_movements[1], 'e2')
enemy19 = Enemy(9,-2,50,  wawe_movements[0], 'e3')
enemy20 = Enemy(120,-2,50, wawe_movements[1], 'e4')
enemy21 = Enemy(150,-20,50, wawe_movements[0], 'e5')
enemy22 = Enemy(180,-20,50, wawe_movements[0], 'e6')
enemy23 = Enemy(200,-2,50, wawe_movements[1], 'e7')
enemy24 = Enemy(220,-20,50, wawe_movements[2], 'e8')


enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10, enemy11, enemy12, enemy13, enemy14, enemy15, enemy16, enemy17, enemy18, enemy19, enemy20, enemy21, enemy22, enemy23, enemy24]

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
            real_pos = player.position + (camera.fov * x, camera.fov * y, 0)

            if shoot == True: # Ha a karakter celoz, mikozbe lo
                direction = [real_pos[0] - player.x,
                             real_pos[1] - player.y, 0]
            if shoot == False: # Ha a karakter nem celoz - eredmeny hogy nagyobb a szoras
                direction = [(real_pos[0] - player.x) + (randint(-500, 500) / 100),
                             (real_pos[1] - player.y) + (randint(-500, 500) / 100), 0]

            duration = 0.03 * (distance(player.position + [20 * p for p in direction], player.world_position))
            bullet = Entity(parent = scene, model = 'sphere', collider = 'box', color = color.black, position = player.position, tag ='projectile', scale = (0.2, 0.2, 0.05))
            bullet.animate_position(player.position + [20 * p for p in direction], duration = duration, curve = curve.linear)
            invoke(destroy, bullet, delay = 1)

            ray = raycast(player.position, direction, distance = 50, ignore = (player, bullet, right, left, up, down), debug = True)
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

player = Player(model='plane', color = color.orange, scale = (1, 1, -1), position = (0, 0.5, 0), rotation = (90, 0, 0), tag ='player')

########################################################################################################################

prev_pos = player.world_position
def slow_check():
    for enemy in enemies:
        if distance(enemy, player) <= 100:  # lotavolsag
            print('lovok')
            #bullet_ray = raycast(enemy.world_position, bullet.forward, distance=10, ignore = [enemy])
            #enemy_bullet.look_at(prev_pos)

    invoke(slow_check, delay = 1)
slow_check()

def update():
    global shoot, movespeed, duration

    for enemy in enemies:
        enemy.look_at_2d(Vec3(enemy.list[enemy.current_move][0],enemy.list[enemy.current_move][1],enemy.list[enemy.current_move][2]))
        if distance(enemy, player) >= 2:
            if enemy.current_move != len(enemy.list): # amig a current_move nem egyenlo a lista hosszaval
                enemy.position += enemy.up * 0.02 # mozgatas

                if enemy.current_move != len(enemy.list) - 1:
                    if round(enemy.position.x, 1) == round(float(enemy.list[enemy.current_move][0]),1): # ellenorzi hogy elerte e a poziciot.
                        if round(enemy.position.y, 1) == round(float(enemy.list[enemy.current_move][1]),1):
                            enemy.current_move += 1 # tovabb lep a kovetkezo pontra.
        else:
            print('kozel')

    # []-------------------------------------------------------------------------[]

    if held_keys['right mouse']:
        shoot = True
        movespeed = 1
    else:
        shoot = False

    #ai
    for i in enemies:
        pass
'''        enemy_hit = i.intersects(debug = True, ignore = (i,))
        if distance(i, lower_body) > 3 and enemy_hit.hit == False:
            i.x += 0.005'''

        #ray = raycast(i.position, -lower_body.world_position, distance=51, ignore=(),debug=True)

########################################################################################################################
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]


camera.add_script(SmoothFollow(target = player, offset=[0, 1, -50], speed=4))

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

tower = Entity(model='cube', collider='mesh', scale=(2,2,0), color = color.violet, x = -8, y = -5, tag = 'tower')
tower = Entity(model='cube', collider='mesh', scale=(2,2,0), color = color.violet, x = -10, y = 3, tag = 'tower')
tower = Entity(model='cube', collider='mesh', scale=(2,2,0), color = color.violet, x =  2, y = 8, tag = 'tower')

app.run()