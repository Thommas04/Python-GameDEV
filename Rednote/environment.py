
from ursina import *
from random import *

stumps_spritesheet = 'textures/seasons/trees/stump_sheet.png'
trees_spritesheet = 'textures/seasons/trees/trees_sheet.png'

# ----------------------------------------------------------------------------------------------------------------------

# oak, maple, pine
types = {'oak' : [0,0],
                 }

class Trees(Entity):
    def __init__(self, type, position, stage = 'stage4', cut = True):

        self.type = types[type]
        self.cut = cut
        self.pos = [position[0] - 0.2, position[1] - 5, position[2]]

        dist = distance([position[0], 0, position[2]], position)

        self.front_layer = -0.12 + (sqrt(dist) / 1000)
        self.back_layer = -0.05 + (sqrt(dist) / 1000)


        if self.cut:
            self.tree_stump = Entity(texture = stumps_spritesheet, model='quad', position = [position[0] - 0.2, position[1] - 5, self.back_layer], alpha = 1, tileset_size = [1, 1], tile_coordinate = self.type,  scale = (3, 3))
            self.tree_crown = Entity(texture = trees_spritesheet,  model='quad', position = position, alpha = 1, tileset_size = [1, 1], tile_coordinate = self.type,  scale = (6.3, 10.2))

        self.tree_collision = Entity(scale = (1.6,1.6), collider = 'box', model = 'quad', position = [position[0] - 0.2, position[1] - 5, -0.1], visible = False)

        if not self.cut:
            pass

