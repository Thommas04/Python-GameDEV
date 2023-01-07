

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

filters.setExposureAdjust(-1)

filters.setHighDynamicRange()
#filters.setSrgbEncode()



Entity(model='plane', scale=10, color=color.gray,
shader=lit_with_shadows_shader)
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True, rotation=(45, -45, 45))

app.run()