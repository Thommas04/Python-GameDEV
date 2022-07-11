
from ursina import *
from ursina import CubicBezier
app = Ursina()

camera.orthographic = True
camera.fov = 16
camera.position = (9, 6)
window.color = color.black

i = 0
for e in dir(curve):
    try:
        item = getattr(curve, e)
        print(item.__name__, ':', item(.75))
        curve_renderer = Entity(
            model=Mesh(vertices=[Vec3(i / 31, item(i / 31), 0) for i in range(32)], mode='line', thickness=2),
            color=color.light_gray)
        row = floor(i / 8)
        curve_renderer.x = (i % 8) * 2.5
        curve_renderer.y = row * 1.75
        label = Text(parent=curve_renderer, text=item.__name__, scale=8, color=color.gray, y=-.1)
        i += 1
    except:
        pass

c = CubicBezier(0, .5, 1, .5)
print('-----------', c.calculate(.23))

window.exit_button.visible = False
window.fps_counter.enabled = False
'''
These are used by Entity when animating, like this:

e = Entity()
e.animate_y(1, curve=curve.in_expo)

e2 = Entity(x=1.5)
e2.animate_y(1, curve=curve.CubicBezier(0,.7,1,.3))
'''

app.run()