
from ursina import *
from panda3d.core import CardMaker
from panda3d.core import PointLight

from direct.showbase.ShowBase import ShowBase

# 1, 0, 0.0001 -> ez középen a legerősebb egy egységig, utána lassan nagyobb (20 egységnyi átmérőben megvilágít mindent)
# 1, 0, 0.02 -> 3-4 egységben megvilágítja a körülötte lévő objektumoka, nem megy távora a fényre.

light_dictionary = {'street_lamp' : ((1, 0, 0.002)),
                    'oil_lamp' : (0.5, 0, 1),
                    }

class LightSource():
    def __init__(self, host, position = [0, 0], attenuation = (0.1, 0.01, 0.0), color = [1,1,1], type = None):
        self.light_node = PointLight('light 1')
        self.light = render.attach_new_node(self.light_node)
        base.render.set_light(self.light)
        self.light.set_pos(position[0], position[1], -1)
        render.setShaderAuto()
        self.light_node.setColor((color[0], color[1], color[2], 10))

        if type == None:
            self.light_node.set_attenuation((0.1, 0.01, 0.0))
        else:
            self.light_node.set_attenuation(light_dictionary[type])

        host.lights_list.append(self)

    #-------------------------------------------------------------------------------------------------------------------
    def new_position(self, x, y):
        self.light.set_pos(x, y, -0.5)

    def turn_off(self):
        pass

    def turn_on(self):
        pass

    def change_color(self):
        pass

    def animate_color(self):
        pass




class LightSystem():
    def __init__(self):
        self.amibent_light = AmbientLight(color = rgb(40,40,42))

    # A Value-t percekben kapjuk meg
    # 6:00 -> 360

    #SEASON SET

    # SPRING
    # SUMMER
    # FALL
    # WINTER

    def time_set(self, value):
        if value == 361:
            self.amibent_light.color = rgb(40,40,42) # Hajnali sötétebb szürkés világítás
            #self.amibent_light.animate_color(rgb(179, 207, 226), duration = 10) # Nappali fény
            self.amibent_light.animate_color(rgb(20, 20, 80), duration=10)

        '''if value == 380: # Kezd lemenni a nap
            self.amibent_light.animate_color(rgb(137,120,93), duration = 10)

        if value == 420: # Este
            self.amibent_light.animate_color(rgb(16, 26, 45), duration = 10)'''

        '''if value == 410: # Este
            self.amibent_light.animate_color(rgb(60, 60, 45), duration = 10)'''