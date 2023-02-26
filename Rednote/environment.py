
from ursina import *
from random import *

stumps_spritesheet = 'textures/seasons/trees/stump_sheet.png'
trees_spritesheet = 'textures/seasons/trees/trees_sheet.png'

rain_spritesheet = 'textures/seasons/weather/rain/rain.png'

# ----------------------------------------------------------------------------------------------------------------------

# oak, maple, pine
types = {'oak' : [0,0],
        }


# ----------------------------------------------------------------------------------------------------------------------

class Trees():
    def on_hover(self):
        self.mouse_on = True
    def on_leave(self):
        self.mouse_on = False

    def __init__(self, player, type, position, matrix, stage = 'stage4', cut = True):
        self.matrix = matrix
        self.type = types[type]
        self.cut = cut
        self.pos = [position[0] - 0.2, position[1], position[2]]
        self.mouse_on = False

        self.alive = True
        self.health = 6

        dist = distance([position[0], 0, position[2]], position)

        self.front_layer = -1 * ( 0.65 - (sqrt(dist) / 100) )
        self.back_layer  = -1 * ( 0.22 - (sqrt(dist) / 100) )

        if self.cut:
            self.tree_stump = Entity(tag = 'none', texture = stumps_spritesheet, model='quad', position = [position[0] - 0.2, position[1], self.front_layer], alpha = 1, tileset_size = [1, 1], tile_coordinate = self.type,  scale = (3, 3))
            self.tree_crown = Entity(tag = 'none', texture = trees_spritesheet,  model='quad', origin = (0,-0.5,0), position = [position[0], position[1], self.front_layer], alpha = 1, tileset_size = [1, 1], tile_coordinate = self.type,  scale = (6.3, 10.2))

            self.cut_spot = Entity(tag = 'none', visible = False, collider = 'box', scale = (1.5, 5), position = [position[0] - 0.2, position[1] + 2, -0.25], model='quad', on_mouse_enter = Func(Trees.on_hover, self), on_mouse_exit = Func(Trees.on_leave, self))

        #///////////////
        self.tree_collision = Entity(scale = (2.5,2), origin = (-0.5,0.5), collider = 'box', model = 'quad', position = [position[0] - 1.5, position[1] + 0.8, -0.1], visible = False, tag = 'tree')

        if not self.cut:
            pass

        player.trees_list.append(self)

# ----------------------------------------------------------------------------------------------------------------------

class Weather():
    def __init__(self):
        self.rain_screen_left = SpriteSheetAnimation(rain_spritesheet, position=[-0.5, 0, 0.3], color = color.white, alpha = 0.1, parent = camera.ui, tileset_size=(30, 1), scale = (1,1) ,fps=30, animations={
            'rain': ((0, 0), (29, 0)),
            'stop_rain': ((0, 0), (0, 0)),
        })

        self.rain_screen_right = SpriteSheetAnimation(rain_spritesheet, position=[0.5, 0, 0.3], color = color.white, alpha=0.1, parent=camera.ui, tileset_size=(30, 1), scale=(1, 1), fps=30, animations={
            'rain': ((0, 0), (29, 0)),
            'stop_rain': ((0, 0), (0, 0)),
        })

        self.rain_screen_left.play_animation('rain')
        self.rain_screen_right.play_animation('rain')

        #self.menu_theme = Audio('sounds/environment/environment_rain.ogg', loop=True, autoplay=True, balance=0.5, volume = 0.1)

    def start_weather(self, type, ):
        pass



























