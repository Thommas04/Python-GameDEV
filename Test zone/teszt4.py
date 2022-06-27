from ursina import *
from ursina.raycaster import raycast

app = Ursina()
EditorCamera()

player = Entity(model='quad', collider='box', color=color.azure, position = (4,0,0), scale = (1,1))
hitbox = Entity(model='quad', collider='box', color=color.red,   x=-4, scale = (2,4))

faceing = 'down'

def update():
    player.direction = Vec3(player.up * (held_keys['w'] - held_keys['s']) + player.right * (held_keys['d'] - held_keys['a'])).normalized()  # get the direction we're trying to walk in.

    origin = player.world_position
    hit_info = boxcast(origin, ignore=(player), distance=.5, debug=True, thickness=(2, 2))
    if not hit_info.hit:
        print('hi')
    else:
        print('got hit')

'''    if not hit_info.hit:

        if held_keys['w']:
            player.y += 5 * time.dt
            faceing = 'up'
        if held_keys['s']:
            player.y -= 5 * time.dt
            faceing = 'down'
        if held_keys['a']:
            player.x -= 5 * time.dt
            faceing = 'left'
        if held_keys['d']:
            player.x += 5 * time.dt
            faceing = 'right'

'''







app.run()