from ursina import *
from direct.stdpy import thread

def LoadingWheel():
    print('tegecii')


app = Ursina()
window.color = color.white
info_text = Text('''Press space to start loading textures''', origin=(0,0), color=color.black)
from ursina.prefabs.health_bar import HealthBar

def load_textures():
    textures_to_load = ['brick', 'shore', 'grass', 'heightmap'] * 50
    bar = HealthBar(max_value=len(textures_to_load), value=0, position=(-.5,-.35,-2), scale_x=1, animation_duration=0, bar_color=color.gray)
    for i, t in enumerate(textures_to_load):
        load_texture(t)
        print(i)
        bar.value = i+1
    # destroy(bar, delay=.01)
    print('loaded textures')

def input(key):
    if key == 'space':
        info_text.enabled = False
        t = time.time()

        try:
            thread.start_new_thread(function=load_textures, args='')
        except Exception as e:
            print('error starting thread', e)

        print('---', time.time()-t)
# load_textures()
# invoke(load_textures, delay=0)
app.run()
