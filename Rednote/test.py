
from ursina import *
from ursina.shaders import lit_with_shadows_shader

app = Ursina()
camera.position()

Entity(model='quad', scale=10, color=color.gray, shader=lit_with_shadows_shader, texture = 'textures\\fisher')
Entity(model='cube', y=1, shader=lit_with_shadows_shader)
pivot = Entity()


#DirectionalLight(parent=pivot, y=0, z=0, shadows=True, rotation=(45, -45, 45))

app.run()