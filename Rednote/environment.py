
from ursina import *
from random import *

stumps_spritesheet = 'textures/seasons/trees/stump_sheet.png'
trees_spritesheet = 'textures/seasons/trees/trees_sheet.png'
saplings_spritesheet = 'textures/seasons/trees/saplings_sheet.png'
static_trees_spritesheet = 'textures/seasons/trees/static_trees_sheet.png'

rain_spritesheet = 'textures/seasons/weather/rain/rain.png'
snow_spritesheet = 'textures/seasons/weather/rain/snow.png'

def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# ----------------------------------------------------------------------------------------------------------------------

# oak, maple, pine

seasons = {'spring' : [0, 0],
           'summer' : [4, 1],
           'fall'   : [8, 2],
           'winter' : [12, 3] }

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

    def __init__(self, player, type, position, matrix, stage = 5, cut = True, by_player = False):
        self.matrix = matrix
        self.player = player
        self.type_ = type
        self.type = types[type]
        self.cut = cut
        self.pos = [position[0] - 0.2, position[1], position[2]]
        self.mouse_on = False
        self.by_player = by_player
        self.stage = stage
        print(self.stage)

        self.alive = True
        self.health = 6

        dist = distance([position[0], 0, position[2]], position)

        randomized = randint(0,100) / 1000
        self.front_layer = 0 - map_range(200 - dist, -100, 300, 0.66, 1) + randomized
        self.back_layer  = 0 - map_range(200 - dist, -100, 300, 0.36, 0.6) + randomized


        print('front_layer', self.front_layer)
        print('back_layer', self.back_layer)

        if self.cut:
            self.tree_stump = Entity(tag = 'none', texture = stumps_spritesheet, model='quad', position = [position[0] - 0.2 + 0.7, position[1] + 1, self.front_layer + 0.01], alpha = 1, tileset_size = [4, 4], tile_coordinate = [self.type[0] + seasons[self.player.season][1], self.type[1]] ,  scale = (2.2, 2.2))
            self.tree_crown = Entity(tag = 'none', texture = trees_spritesheet,  model='quad', origin = (0,-0.5,0), position = [position[0] - 0.13 + 0.7, position[1] - 0.1 + 1, self.front_layer], alpha = 1, tileset_size = [4, 4], tile_coordinate = [self.type[0] + seasons[self.player.season][1], self.type[1]],  scale = (4.4, 7.12))

            self.cut_spot = Entity(tag = 'none', visible = False, collider = 'box', scale = (1.5, 5), position = [position[0] - 0.2 + 0.7, position[1] + 2 + 1, -2], model='quad', on_mouse_enter = Func(Trees.on_hover, self), on_mouse_exit = Func(Trees.on_leave, self))




        #///////////////
        self.tree_collision = Entity(visible = False, scale = (1.5,1), origin = (-0.5,0.5), collider = 'box', model = 'quad', position = [position[0] - 0.94 + 0.7, position[1] + 1, -0.1], tag = 'tree')

        if self.by_player == True:
            self.tree_stump.tileset_size = [16, 4]
            self.tree_stump.texture = saplings_spritesheet
            self.tree_stump.tile_coordinate = [self.type[0] + seasons[self.player.season][0], self.type[1]]

            self.tree_crown.visible = False
            self.tree_collision.disable()
            self.cut_spot.scale = (1.5, 1.5)

        if not self.cut:
            pass

        player.trees_list.append(self)

    def upgrade_tree(self, stage):
        if stage == 1:
            self.tree_stump.tileset_size = [16, 4]
            self.tree_stump.texture = saplings_spritesheet
            self.tree_stump.tile_coordinate = [self.type[0] + seasons[self.player.season][0], self.type[1]]

            self.tree_crown.visible = False
            self.tree_collision.disable()
            self.cut_spot.scale = (1.5, 1.5)

        if stage == 2:
            self.tree_stump.tileset_size = [16, 4]
            self.tree_stump.texture = saplings_spritesheet
            self.tree_stump.tile_coordinate = [self.type[0] + seasons[self.player.season][0] + 1, self.type[1]]
            print('tile_coord:',self.tree_stump.tile_coordinate )
            print('type[1]:', self.type[0])
            print('seasons:', seasons[self.player.season][0])

            self.tree_crown.visible = False
            self.tree_collision.disable()
            self.cut_spot.scale = (1.5, 1.5)

        if stage == 3:
            self.tree_stump.tileset_size = [16, 4]
            self.tree_stump.texture = saplings_spritesheet
            self.tree_stump.tile_coordinate = [self.type[0] + seasons[self.player.season][0] + 2, self.type[1]]

            self.tree_crown.visible = False
            self.tree_collision.enable()
            self.cut_spot.scale = (1.5, 2)

        if stage == 4:
            self.tree_stump.tileset_size = [16, 4]
            self.tree_stump.texture = saplings_spritesheet
            self.tree_stump.tile_coordinate = [self.type[0] + seasons[self.player.season][0] + 3, self.type[1]]

            self.tree_crown.visible = False
            self.tree_collision.enable()
            self.cut_spot.scale = (1.5, 2)

        if stage == 5:
            self.tree_stump.tileset_size = [4, 4]
            self.tree_stump.texture = stumps_spritesheet
            self.tree_stump.tile_coordinate = [self.type[0] + seasons[self.player.season][1], self.type[1]]

            self.tree_crown.visible = True
            self.tree_crown.tile_coordinate = [self.type[0] + seasons[self.player.season][1], self.type[1]]
            self.tree_collision.enable()
            self.cut_spot.scale = (1.5, 5)



# ----------------------------------------------------------------------------------------------------------------------

class Weather():
    def __init__(self, player):
        self.player = player
        self.rain_screen_left = SpriteSheetAnimation(texture = rain_spritesheet, position=[-0.5, 0, 0.3], color = color.white, alpha = 0, parent = camera.ui, tileset_size=(30, 1), scale = (1,1) ,fps=30, animations={
            'rain': ((0, 0), (29, 0)),
            'stop_rain': ((0, 0), (0, 0)),
            'start_snow': ((0, 0), (97, 0)),
            'stop_snow': ((0, 0), (0, 0)),
        })

        self.rain_screen_right = SpriteSheetAnimation(texture = rain_spritesheet, position=[0.5, 0, 0.3], color = color.white, alpha=0, parent=camera.ui, tileset_size=(30, 1), scale=(1, 1), fps=30, animations={
            'rain': ((0, 0), (29, 0)),
            'stop_rain': ((0, 0), (0, 0)),
            'start_snow': ((0, 0), (97, 0)),
            'stop_snow': ((0, 0), (0, 0)),
        })


    def start_weather(self):
        if self.player.season != 'winter':
            self.rain_screen_right.fps = 30

            self.rain_screen_right.texture = rain_spritesheet
            self.rain_screen_left.texture = rain_spritesheet

            self.rain_screen_left.play_animation('rain')
            self.rain_screen_right.play_animation('rain')
            self.rain_screen_right.alpha = 0.3
            self.rain_screen_left.alpha = 0.3

            self.menu_theme = Audio('sounds/environment/environment_rain.ogg', loop=True, autoplay=True, balance=0.5, volume = 0.1)

        else:
            self.rain_screen_right.fps = 10

            self.rain_screen_right.texture = snow_spritesheet
            self.rain_screen_left.texture = snow_spritesheet

            self.rain_screen_left.play_animation('start_snow')
            self.rain_screen_right.play_animation('start_snow')
            self.rain_screen_right.alpha = 0.5
            self.rain_screen_left.alpha = 0.5

            self.menu_theme.fade_out(value=0, duration=.2, delay=0, curve=curve.in_expo, resolution=None,interrupt='finish', )

    def stop_weather(self):
        self.rain_screen_left.play_animation('stop_rain')
        self.rain_screen_right.play_animation('stop_rain')
        self.rain_screen_right.alpha = 0
        self.rain_screen_left.alpha = 0

        self.menu_theme.fade_out(value=0, duration=.5, delay=0, curve=curve.in_expo, resolution=None, interrupt='finish', )




























