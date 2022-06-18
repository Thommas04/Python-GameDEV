from ursina import *
from ursina.prefabs import first_person_controller
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()

platform = Entity(model = 'Plane', collider = 'mesh', texture = 'textures\\ground', scale = 10, position = (0, -10, 0))
for i in range(100):
    if i % 3 == 0:
        for b in range(100):
            if b % 3 == 0 :
                    platform = Entity(model = 'Cube', collider = 'mesh', texture = 'textures\\ground', scale = 2, position = (i, -5, b))

app.run()