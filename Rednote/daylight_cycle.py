
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

# ----------------------------------------------------------------------------------------------------------------------

class LightSystem():
    def __init__(self, player):
        self.player = player
        self.ambient_light = AmbientLight(color = rgb(40, 40, 42))

    # A Value-t percekben kapjuk meg
    # 6:00 -> 360

    #SEASON SET

    # SPRING
    # SUMMER
    # FALL
    # WINTER

        self.difference = {'spring' : [361, 960, 1140],
                           'summer' : [361, 1050, 1230],
                           'fall'   : [390, 840, 990],
                           'winter' : [440, 780, 900]
                          }


    def stop_time(self):
        self.light_animation.pause()
    def start_time(self):
        self.light_animation.resume()

    def time_set(self, value):
        if value == self.difference[self.player.season][0]: # kivilágosodik
            self.light_animation = self.ambient_light.animate_color(rgb(179, 207, 226), duration = 60) # Nappali fény

        if value == self.difference[self.player.season][1]: # Kezd lemenni a nap
            self.light_animation = self.ambient_light.animate_color(rgb(137, 120, 93), duration = 60)

        if value == self.difference[self.player.season][2]: # Sötét este
            self.light_animation = self.ambient_light.animate_color(rgb(16, 26, 45), duration = 60)

