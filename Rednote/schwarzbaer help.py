import sys
from ursina import *
from panda3d.core import CardMaker
from panda3d.core import PointLight

from direct.showbase.ShowBase import ShowBase


app = Ursina()
EditorCamera()

base.disable_mouse()
base.accept('escape', sys.exit)

'''maker = CardMaker('card')
card = base.render.attach_new_node(maker.generate())
#texture
map_texture = base.loader.load_texture("main_tile1.png")
# set
#card.set_texture(map_texture)'''

world_canvas = Entity(texture = 'textures/seasons/map/rustfort_summer.png', origin = (-0.5, -0.5, 0), model = 'quad', collider = 'box', scale = (100,100,0), position = (0,0,0), tag = 'canvas')


light_node = PointLight('light 0')
light_node.set_attenuation((-12, 120, 30))
light = render.attach_new_node(light_node)
base.render.set_light(light)
light.set_pos(5, 5, -0.15)
render.setShaderAuto()

light_node1 = PointLight('light 1')
light_node1.set_attenuation((0.1, 0.01, 0.0))

light1 = render.attach_new_node(light_node1)
base.render.set_light(light1)
light1.set_pos(25, 60, -0.15)
render.setShaderAuto()
light_node1.setColor((1, 0, 1, 0))

amibent_light = AmbientLight(color = rgb(12,12,12))

# --------------------------------------------------

from panda3d.core import PointLight, CardMaker

# Létrehozza a PointLight objektumot
light = PointLight('light')
light.setColor((1, 1, 1, 1))
light.setAttenuation((0, 0, 1))
light.setShadowCaster(True, 512, 512)

# Létrehozza a négyzet alakú geometriát
cardMaker = CardMaker('card')
cardMaker.setFrame(-0.5, 0.5, -0.5, 0.5)
card = render.attachNewNode(cardMaker.generate())
card.setPos(0, 0, 0)

# Létrehozza a PointLight objektumot a négyzet alakú geometria felett
lightNP = render.attachNewNode(light)
lightNP.setPos(0, 0, -1)

# Adja hozzá a fényt a világításhoz és beállítja az árnyék projektálását
render.setLight(lightNP)
card.setShaderInput("light", lightNP)

base.run()

# (-1, 1, 10)

# a 3. befolyásolja a fekete pöttyöt