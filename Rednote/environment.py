
from ursina import *
from random import *

stumps_spritesheet = 'textures/seasons/trees/stump_sheet.png'
trees_spritesheet = 'textures/seasons/trees/trees_sheet.png'

rain_spritesheet = 'textures/seasons/weather/rain/rain.png'

# ----------------------------------------------------------------------------------------------------------------------

# oak, maple, pine

seasons = {'spring' : 0,
           'summer' : 4,
           'fall'   : 8,
           'winter' : 12 }

types = {'oak' : [0,0],
         'maple' : [0,1],
         'pine' : [0,2],
         'mahagoni' : [0,3]
        }


# ----------------------------------------------------------------------------------------------------------------------

class Trees():
    def on_hover(self):
        self.mouse_on = True
    def on_leave(self):
        self.mouse_on = False

    def __init__(self, player, type, position, matrix, stage = 4, cut = True):
        self.matrix = matrix
        self.type = types[type]
        self.cut = cut
        self.pos = [position[0] - 0.2, position[1], position[2]]
        self.mouse_on = False

        self.alive = True
        self.health = 6

        dist = distance([position[0], 0, position[2]], position)

        self.front_layer = -1 * ( 2.8 - (sqrt(dist) / 10) )
        self.back_layer  = -1 * ( 1.2 - (sqrt(dist) / 10) )

        if self.cut:
            self.tree_stump = Entity(tag = 'none', texture = stumps_spritesheet, model='quad', position = [position[0] - 0.2, position[1], self.front_layer], alpha = 1, tileset_size = [4, 4], tile_coordinate = self.type,  scale = (2.2, 2.2))
            self.tree_crown = Entity(tag = 'none', texture = trees_spritesheet,  model='quad', origin = (0,-0.5,0), position = [position[0] - 0.13, position[1] - 0.1, self.front_layer - 1], alpha = 1, tileset_size = [4, 4], tile_coordinate = self.type,  scale = (4.4, 7.12))

            self.cut_spot = Entity(tag = 'none', visible = False, collider = 'box', scale = (1.5, 5), position = [position[0] - 0.2, position[1] + 2, -0.25], model='quad', on_mouse_enter = Func(Trees.on_hover, self), on_mouse_exit = Func(Trees.on_leave, self))

        #///////////////
        self.tree_collision = Entity(visible = False, scale = (1.5,1), origin = (-0.5,0.5), collider = 'box', model = 'quad', position = [position[0] - 0.94, position[1], -0.1], tag = 'tree')

        if not self.cut:
            pass

        player.trees_list.append(self)

# ----------------------------------------------------------------------------------------------------------------------

class Weather():
    def __init__(self):
        self.rain_screen_left = SpriteSheetAnimation(rain_spritesheet, position=[-0.5, 0, 0.3], color = color.white, alpha = 0, parent = camera.ui, tileset_size=(30, 1), scale = (1,1) ,fps=30, animations={
            'rain': ((0, 0), (29, 0)),
            'stop_rain': ((0, 0), (0, 0)),
        })

        self.rain_screen_right = SpriteSheetAnimation(rain_spritesheet, position=[0.5, 0, 0.3], color = color.white, alpha=0, parent=camera.ui, tileset_size=(30, 1), scale=(1, 1), fps=30, animations={
            'rain': ((0, 0), (29, 0)),
            'stop_rain': ((0, 0), (0, 0)),
        })

        self.rain_screen_left.play_animation('rain')
        self.rain_screen_right.play_animation('rain')

        #self.menu_theme = Audio('sounds/environment/environment_rain.ogg', loop=True, autoplay=True, balance=0.5, volume = 0.1)

    def start_weather(self, type, ):
        pass



























