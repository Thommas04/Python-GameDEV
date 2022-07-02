
from ursina import *

def create_net():
    x = -101 ; y = -101
    for i in range(200):
        x += 1 ; y += 1
        line_x = Entity(model = Mesh (vertices = [Vec3(x, -100, 0), Vec3(x, 100, 0)], mode = 'line', thickness = 1), z = -0.2, color = color.orange)
        text_x = Text(parent = line_x, text = str(x), position = (x, 0, 0), scale = 10)
        line_y = Entity(model = Mesh (vertices = [Vec3(-100, y, 0), Vec3(100, y, 0)], mode = 'line', thickness = 1), z = -0.2, color = color.orange)
        text_y = Text(parent=line_y, text = str(y), position = (0, y, 0), scale = 10)

    line_x = Entity(model = Mesh(vertices = [Vec3(0, -100, 0), Vec3(0, 100, 0)], mode = 'line', thickness = 3), z = -0.22, color = color.blue)
    line_y = Entity(model = Mesh(vertices = [Vec3(-100, 0, 0), Vec3(100, 0, 0)], mode = 'line', thickness = 3), z = -0.22, color = color.blue)

def input(key):
    if key == 'left mouse down':
        try:
            print("(", round(mouse.world_point.x,2),", ", round(mouse.world_point.y,2) ,", ", 0 , "),", sep = "")
            Text(parent = scene, world_position = (mouse.world_point.x, mouse.world_point.y, -0.001 ), scale = 10, text = str(round(mouse.world_point.x,2)) + " / " + str(round(mouse.world_point.y,2)))
            Entity(parent = scene, model = 'sphere', color = color.red, scale = 0.1, world_position = (mouse.world_point.x, mouse.world_point.y, 0 )  )
        except: pass