
from ursina import *
import ursina.prefabs.trail_renderer
app = Ursina()

window.color = color.black
mouse.visible = False
player = Entity()
player.graphics = Entity(parent=player, scale=.1, model='circle')
trail_renderer = TrailRenderer(parent=player, thickness=100, color=color.yellow, length=6)

pivot = Entity(parent=player)
trail_renderer = TrailRenderer(parent=pivot, x=.1, thickness=20, color=color.orange)
trail_renderer = TrailRenderer(parent=pivot, y=1, thickness=20, color=color.orange)
trail_renderer = TrailRenderer(parent=pivot, thickness=2, color=color.orange, alpha=.5, position=(.4,.8))
trail_renderer = TrailRenderer(parent=pivot, thickness=2, color=color.orange, alpha=.5, position=(-.5,.7))

def update():
    player.position = lerp(player.position, mouse.position*10, time.dt*4)

    if pivot:
        pivot.rotation_z -= 3
        pivot.rotation_x -= 2

def input(key):
    if key == 'space':
        destroy(pivot)


app.run()