
from ursina import *
from ursina.shaders import lit_with_shadows_shader

app = Ursina()
camera.position()

Entity(model='quad', scale=10, color=color.gray, shader=lit_with_shadows_shader, texture = 'textures\\fisher')
Entity(model='cube', y=1, shader=lit_with_shadows_shader)
pivot = Entity()


# fények - késõbb készíthetõ belõle napszakváltás, évszakok stb.

#L1 = PointLight(y = -2, z = 2, color = color.black, scale = 10)
#L2 = PointLight(y = -5, z = 10, color = color.blue, scale = 100)
L3 = PointLight(y = 10,x = 2, z = 1, color = color.white, scale = 1)

#DirectionalLight(parent=pivot, y=0, z=0, shadows=True, rotation=(45, -45, 45))

app.run()