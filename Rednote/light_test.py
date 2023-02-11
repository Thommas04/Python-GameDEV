from ursina import *

mymap = 'textures/seasons/map/rustfort_summer.png'
app = Ursina()

EditorCamera()

from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath
from panda3d.core import PointLight
from panda3d.core import LVector3
import math
import sys
import colorsys

class Light_test(Entity):
    def __init__(self):


        self.redHelper = loader.loadModel("models/sphere")
        self.redHelper.setColor((1, 0, 0, 1))
        self.redHelper.setPos(0, 0, 0)
        self.redHelper.setScale(.25)
        self.redPointLight = self.redHelper.attachNewNode(PointLight("redPointLight"))
        self.redPointLight.node().setColor((.35, 0, 0, 10))
        self.redPointLight.node().setAttenuation(LVector3(0, 0.04, -0))

        self.pointLightHelper = render.attachNewNode("pointLightHelper")
        self.pointLightHelper.setPos(25, 0, -10)
        self.redHelper.reparentTo(self.pointLightHelper)

        render.setLight(self.redPointLight)

        self.perPixelEnabled = False
        self.shadowsEnabled = False

world_canvas = Entity(texture = mymap, model = 'cube', collider = 'box', scale = (50,50,0), position = (0,0,0), tag = 'canvas')

test = Light_test()

app.run()