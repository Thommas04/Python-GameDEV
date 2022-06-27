from ursina import *

app = Ursina()

verts = ((17.22, -0.14, 0),(18.6, -0.21, 0),(17.54, 3.24, 0),(17.54, 3.26, 0),(18.74, -0.46, 0),(22.03, -0.48, 0),(22.03, -0.46, 0),(21.85, 3.21, 0),(17.54, 3.26, 0),(21.85, 3.21, 0),(22.05, -0.17, 0),(27.15, -0.21, 0),(27.15, -0.21, 0),(21.85, 3.21, 0),(26.36, 3.1, 0),(21.85, 3.14, 0),(27.11, -0.18, 0),(26.58, 3.16, 0))
tris = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)


player = Entity(model='plane', color=color.orange, collider='box', origin_y=-.5, rotation = (-90, 0, 0), position = (5, 2, 0))

trigger_box = Entity(model='plane', color=color.red, scale=2, collider='mesh', rotation = (-90, 0, 0), origin_y=-.5)
EditorCamera()

def update():
    direction = Vec3(player.forward * (held_keys['w'] - held_keys['s']) + player.right * (held_keys['d'] - held_keys['a']))

    if player.intersects(trigger_box, debug = True).hit:
        trigger_box.color = color.lime
        player.position += direction * 5 * time.dt
        print('player is inside trigger box')


app.run()