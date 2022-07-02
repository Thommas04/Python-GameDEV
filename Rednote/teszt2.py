from ursina import *
from ursina.raycaster import raycast
from functions import *

app = Ursina()
EditorCamera()

#create_net()

class Player(Entity):
    def update(self):
        right_hit = right.intersects(debug = False, ignore = (right, left, up, down))
        left_hit = left.intersects(debug=False, ignore = (right, left, up, down))
        up_hit = up.intersects(debug=False, ignore = (right, left, up, down))
        down_hit = down.intersects(debug=False, ignore = (right, left, up, down))

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
            right_hit.entity.color = color.pink

        if left_hit.hit == False:
            right.x -= held_keys['a'] * movespeed * time.dt
            left.x -= held_keys['a'] * movespeed * time.dt
            up.x -= held_keys['a'] * movespeed * time.dt
            down.x -= held_keys['a'] * movespeed * time.dt
            self.x -= held_keys['a'] * movespeed * time.dt
        else:
            left_hit.entity.color = color.pink

        if up_hit.hit == False:
            right.y += held_keys['w'] * movespeed * time.dt
            left.y += held_keys['w'] * movespeed * time.dt
            up.y += held_keys['w'] * movespeed * time.dt
            down.y += held_keys['w'] * movespeed * time.dt
            self.y += held_keys['w'] * movespeed * time.dt
        else:
            up_hit.entity.color = color.pink

        if down_hit.hit == False:
            right.y -= held_keys['s'] * movespeed * time.dt
            left.y -= held_keys['s'] * movespeed * time.dt
            up.y -= held_keys['s'] * movespeed * time.dt
            down.y -= held_keys['s'] * movespeed * time.dt
            self.y -= held_keys['s'] * movespeed * time.dt
        else:
            down_hit.entity.color = color.pink



# [][][][][][][][][][][][][][][][][][][][][]

lower_body = Player(model='plane', color = color.orange, scale = (1,1,-1), position = (0,0.5,0), rotation = (90,0,0))

right = Entity(model='plane', scale=(0.1, 1, -1), position = (0.5, 0.5, 0), color = color.red, rotation = (90,0,0), collider='box')
left = Entity(model='plane', scale=(0.1, 1, -1), position = (-0.5, 0.5, 0), color = color.brown, rotation = (90,0,0), collider='box')
up = Entity(model='plane', scale=(1, 1, -0.1), position = (0, 1, 0), color = color.azure, rotation = (90,0,0), collider='box')
down = Entity(model='plane', scale=(1, 1, -0.1), position = (0, 0, 0), color = color.pink, rotation = (90,0,0), collider='box')

Entity(model='cube', collider='mesh', scale=(3,5,0), color = color.azure, x = -7, y = 2)
Entity(model='cube', collider='mesh', scale=(1,1,0), color = color.red, x = -3, y = 3.6)
Entity(model='cube', collider='mesh', scale=(1,1,0), color = color.red, x = -2.3, y = 0)

Entity(model='cube', collider='mesh', scale=(1,4,0), color = color.red, x = -2, y = 0)

Entity(model='cube', collider='mesh', scale=(1,2,0), color = color.red, x = -3, y = -1)

Entity(model='cube', collider='mesh', scale=(5,5,0), color = color.azure, x = 8, y = 2)

app.run()