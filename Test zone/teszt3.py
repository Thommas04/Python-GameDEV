from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from random import randint
app = Ursina()
ground = Entity(model='cube',scale=(15,1,1),collider='box')
next_platform_y = 4
player = PlatformerController2d(scale_y=2, jump_height=4, x=3, y=2)
score = Text("Score:"+str(floor(player.y)),position=(-.5,0.45))
platforms = [ground]
platforms_max = platforms[len(platforms)-1]
platforms_min = platforms[0]
def gen_platform(x,y):
    x = randint((x-5),(x+5))
    while abs(x) > 6:
        x = randint((x-5),(x+5))
    platforms.append(Entity(model='cube',scale=(2,1,1),position=(x,y,0),collider='box'))
def game_over():
    Text("Game Over")
    application.pause()
def update():
    global platforms_max,next_platform_y
    camera.y = player.y
    score.text = "Score:"+str(floor(player.y))
    try:
        platforms_max = platforms[len(platforms)-1]
        platforms_min = platforms[0]
    except IndexError:
        game_over()
        return
    if held_keys['space']: player.jump()
    if platforms_max.y - player.y < 6:
        gen_platform(platforms[len(platforms)-1].x,next_platform_y)
        next_platform_y += 4
    if abs(platforms_min.y - player.y) > 13:
        destroy(platforms[0])
        del platforms[0]
app.run()