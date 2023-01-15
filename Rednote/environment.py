
from ursina import *
from random import *

stumps_spritesheet = 'textures/seasons/trees/stump_sheet.png'
trees_spritesheet = 'textures/seasons/trees/trees_sheet.png'

# ----------------------------------------------------------------------------------------------------------------------

# oak, maple, pine
types = {'oak' : [0,0],
                 }

class Trees(Entity):
    def on_hover(self):
        self.mouse_on = True
        print(self.mouse_on)
    def on_leave(self):
        self.mouse_on = False
        print(self.mouse_on)

    def __init__(self, type, position, matrix, stage = 'stage4', cut = True):
        self.matrix = matrix
        self.type = types[type]
        self.cut = cut
        self.pos = [position[0] - 0.2, position[1], position[2]]
        self.mouse_on = False

        self.alive = True
        self.health = 6

        dist = distance([position[0], 0, position[2]], position)

        self.front_layer = -1 * ( 0.24 - (sqrt(dist) / 100) )
        self.back_layer  = -1 * ( 0.12 - (sqrt(dist) / 100) )

        if self.cut:
            self.tree_stump = Entity(texture = stumps_spritesheet, model='quad', position = [position[0] - 0.2, position[1], self.front_layer -0.02], alpha = 1, tileset_size = [1, 1], tile_coordinate = self.type,  scale = (3, 3))
            self.tree_crown = Entity(texture = trees_spritesheet,  model='quad', origin = (0,-0.5,0), position = [position[0], position[1], self.front_layer], alpha = 1, tileset_size = [1, 1], tile_coordinate = self.type,  scale = (6.3, 10.2))

            self.cut_spot = Entity(visible = False, collider = 'box', scale = (1.5, 5), position = [position[0] - 0.2, position[1] + 2, -0.25], model='quad', on_mouse_enter = Func(Trees.on_hover, self), on_mouse_exit = Func(Trees.on_leave, self))

        #///////////////
        self.tree_collision = Entity(scale = (1.6,1.6), collider = 'box', model = 'quad', position = [position[0] - 0.2, position[1], -0.1], visible = False)

        if not self.cut:
            pass
