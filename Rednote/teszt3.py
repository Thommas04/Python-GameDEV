from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(model='plane', texture='grass', scale=20, collider='box')
wall = Entity(model='cube', origin_y=-.5, position=(0,0,5), scale=(5,3,1), texture='brick', collider='box')
wall_2 = Entity(model='cube', origin_y=-.5, position=(-3,0,5), scale=(5,3,1), texture='brick', collider='box', rotation_y=-30)

player = FirstPersonController()

decals = LoopingList([Entity(model='quad', texture='radial_gradient', color=color.red, x=1000) for i in range(100)])
decals.i = 0

def input(key):
    if key == 'left mouse down' and mouse.world_point:
        decals[decals.i].position = mouse.world_point + mouse.world_normal*.01
        decals[decals.i].look_at(mouse.world_point + mouse.world_normal, axis='back')
        decals.i += 1

app.run()

###########################################################################

from ursina import *
from ursina.shaders import lit_with_shadows_shader
from direct.filter.CommonFilters import CommonFilters

app = Ursina()
EditorCamera()

a = Entity(model='cube', y=1, shader=lit_with_shadows_shader)

filters = CommonFilters(base.win, base.cam)

#filters.setBloom(blend = (1,1,0.,0.1))
#filters.setVolumetricLighting(caster = camera, numsamples= 10, density= 1, decay=0.1, exposure= 0.2)
#filters.setBlurSharpen(amount = 0)
#filters.setAmbientOcclusion()
#filters.setGammaAdjust(1.5)

#filters.setExposureAdjust(-1)

filters.setHighDynamicRange()
#filters.setSrgbEncode()



Entity(model='plane', scale=10, color=color.gray,
shader=lit_with_shadows_shader)
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))

app.run()