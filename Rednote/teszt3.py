from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(model='plane', texture='grass', scale=20, collider='box')
wall = Entity(model='cube', origin_y=-.5, position=(0,0,5), scale=(5,3,1), texture='brick', collider='box')
wall_2 = Entity(model='cube', origin_y=-.5, position=(-3,0,5), scale=(5,3,1), texture='brick', collider='box', rotation_y=-30)

player = FirstPersonController()

decals = LoopingList([Entity(model='quad', texture='radial_gradient', color=color.red, x=1000) for i in range(100)])
decals.i = 0

def input(key):
    if key == 'left mouse down' and mouse.world_point:
        decals[decals.i].position = mouse.world_point + mouse.world_normal*.01
        decals[decals.i].look_at(mouse.world_point + mouse.world_normal, axis='back')
        decals.i += 1

app.run()