from ursina import *
from direct.stdpy import thread


app = Ursina()
window.color = color.white

Button.color = color._20


te = TextField(max_lines=1, scale=1, register_mouse_input = True, text='1234')



entity = Entity(model = 'cube', scale = 1, color = color.red, position = (0,0,0))

def func():
    entity.animate_position((0,5,0), duration = 10, curve = curve.linear)


def update():
    print('tekocog')

thread.start_new_thread(function=func, args='')


app.run()