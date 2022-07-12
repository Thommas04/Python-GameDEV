from ursina import *
from ursina.raycaster import raycast
from functions import *
from random import *

app = Ursina()
#EditorCamera()

background = Entity(model = 'cube', collider = 'box', scale = (1000,1000,0), color = color.dark_gray, position = (0,0,0.1))


#6create_net()

class Enemy(Entity):
    def __init__(self, x, y, hp, **kwargs):
        super().__init__(self, **kwargs)
        self.x = x
        self.y = y
        self.hp = hp





########################################################################################################################

enemy1 = Enemy(10,5,50, model='plane', color = color.orange, scale = (1, 1, -1), position = (0, 0, 0), rotation = (90, 0, 0), tag = 'enemy')
enemy2 = Enemy(1,5,50,model='plane', color = color.orange, scale = (1, 1, -1), position = (2, -3, 0), rotation = (90, 0, 0), tag = 'enemy')


enemy3 = Enemy(15,0,50,model='plane', color = color.orange, scale = (1, 1, -1), position = (4, -3, 0), rotation = (90, 0, 0), tag = 'enemy')
enemy4 = Enemy(20,5,50,model='plane', color = color.orange, scale = (1, 1, -1), position = (6, -3, 0), rotation = (90, 0, 0), tag = 'enemy')
enemy5 = Enemy(25,2,50,model='plane', color = color.orange, scale = (1, 1, -1), position = (8, -3, 0), rotation = (90, 0, 0), tag = 'enemy')
enemy6 = Enemy(30,5,50,model='plane', color = color.orange, scale = (1, 1, -1), position = (10, -3, 0), rotation = (90, 0, 0), tag = 'enemy')
enemy7 = Enemy(40,5,50,model='plane', color = color.orange, scale = (1, 1, -1), position = (12, -3, 0), rotation = (90, 0, 0), tag = 'enemy')
enemy8 = Enemy(45,5,50,model='plane', color = color.orange, scale = (1, 1, -1), position = (14, -3, 0), rotation = (90, 0, 0), tag = 'enemy')


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

def input(key):
    global pull_up, revolver_ammo, full_ammo
    if key == 'left mouse down':
        if pull_up == True and revolver_ammo > 0:
            x, y, z = mouse.position
            real_pos = lower_body.position + (camera.fov * x, camera.fov * y, 0)

            if shoot == True: # Ha a karakter celoz, mikozbe lo
                direction = [real_pos[0] - lower_body.x, real_pos[1] - lower_body.y, 0]
            if shoot == False: # Ha a karakter nem celoz - eredmeny hogy nagyobb a szoras
                direction = [(real_pos[0] - lower_body.x) + (randint(-500,500) / 100),
                             (real_pos[1] - lower_body.y) + (randint(-500,500) / 100), 0]

            duration = 0.03 * (distance(lower_body.position + [20 * p for p in direction], lower_body.world_position))
            bullet = Entity(parent = scene, model = 'sphere', collider = 'box', color = color.black, position = lower_body.position, tag = 'projectile', scale = (0.2, 0.2, 0.05))
            bullet.animate_position(lower_body.position + [20 * p for p in direction], duration = duration, curve = curve.linear)
            invoke(destroy, bullet, delay = 1)

            ray = raycast(lower_body.position, direction, distance = 50, ignore = (lower_body, bullet, right, left, up, down), debug = False)
            if ray.hit:
                if ray.entity.tag == 'building':
                    destroy(bullet, delay = ray.distance * 0.035)

            pull_up = False
            revolver_ammo -= 1
            invoke(pull_up_delay, delay = revolver_shoot_speed)
            #print('\nra:',revolver_ammo)

    if key == 'r': # reload
        for i in range(10 - revolver_ammo):
            if full_ammo > 0:
                full_ammo -= 1
                revolver_ammo += 1

        print('--------------------\nfa:', full_ammo, '\nra:',revolver_ammo)

def update():
    global shoot, movespeed
    if held_keys['right mouse']:
        shoot = True
        movespeed = 1
    else:
        shoot = False

########################################################################################################################

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



# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

lower_body = Player(model='plane', color = color.orange, scale = (1,1,-1), position = (0,0.5,0), rotation = (90,0,0), tag = 'player')

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

tower = Entity(model='cube', collider='mesh', scale=(2,2,0), color = color.red, x = -8, y = 0, tag = 'tower')
tower = Entity(model='cube', collider='mesh', scale=(2,2,0), color = color.red, x = -10, y = -3, tag = 'tower')
tower = Entity(model='cube', collider='mesh', scale=(2,2,0), color = color.red, x =  2, y = 10, tag = 'tower')

#Artif.enemy_go_to(Tomi2, 5, 8)

app.run()