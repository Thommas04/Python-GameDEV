from ursina import *


app = Ursina()

slider = Entity(model='quad', color=color.red, scale_x=0.1, scale_y=2)
slider.speed = 0

def update():
    if mouse.left:
        slider.speed = 10
    else:
        slider.speed -= 0.1
        slider.y -= slider.speed

def on_mouse_down():
    if slider.collision(mouse.point, 0.1):
        slider.speed = 10

EditorCamera()
app.run()