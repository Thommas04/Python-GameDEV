import math
from ursina import *

# Set up the window
app = Ursina()

center = Entity(model='quad', scale=.1, color=color.red)
p = Entity()
for i in range(4*5):
    b = Button(parent=p, model='quad', scale=Vec2(.2,.1), text=str(i), color=color.tint(color.random_color(),-.6))
    b.text_entity.scale=1
t = time.time()
grid_layout(p.children, max_x=7, max_y=10, origin=(0, .5), spacing=(.15, 0))
center = Entity(parent=camera.ui, model=Circle(), scale=.005, color=color.lime)
EditorCamera()
print(time.time() - t)

app.run()