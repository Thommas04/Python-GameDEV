
from ursina import *

class LightSystem():
    def __init__(self):
        self.amibent_light = AmbientLight(color = color.dark_gray)


    # A Value-t percekben kapjuk meg
    # 6:00 -> 360

    #SEASON SET

    def time_set(self, value):
        if value == 361:
            self.amibent_light.color = rgb(40,40,42) # Hajnali sötétebb szürkés világítás
            self.amibent_light.animate_color(rgb(179, 207, 226), duration = 10) # Nappali fény

        if value == 420: # Kezd lemenni a nap
            self.amibent_light.animate_color(rgb(137,120,93), duration = 10)

        if value == 480: # Este
            self.amibent_light.animate_color(rgb(16, 26, 45), duration = 10)
