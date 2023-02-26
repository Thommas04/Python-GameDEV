from panda3d.core import PointLight, VBase4
from direct.showbase.ShowBase import ShowBase
from ursina import *



class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Létrehozza a point light-ot
        plight = PointLight("plight")
        plight.setColor(VBase4(1, 1, 1, 1))
        plight.setAttenuation((1, 0, 0))
        plnp = self.render.attachNewNode(plight)
        plnp.setPos(5, 4, 0)
        self.render.setLight(plnp)

        # Teljesen elsötétíti a fényt
        plight.setColor(VBase4(0, 0, 0, 1))


app = MyApp()
app.run()