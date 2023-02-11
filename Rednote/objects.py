
# REDNOTE - OBJECTS
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] #

from ursina import *

#TEXTURES
rusfort_bank_texture = 'textures/buildings/rustfort_bank.png'
tent_texture = 'textures/buildings/tent.png'
church_texture = 'textures/buildings/church.png'

static_z_axis = -0.18
z_axis_hovered = -0.16
z_axis_lowered = -0.12

class InteractiveObject(Entity):
    def __init__(self, x, y, tag, parent, height, scale = (1, 1, -1)):
        super().__init__(self, **kwargs)
        self.model = 'quad'
        self.scale = scale
        self.parent = parent
        self.rotation = (90, 0, 0)
        self.position = [x, y, -0.1]
        self.tag = tag
        self.alpha = 0

    def update(self):
        print('geci')



def place_buildings(player):

    tent_obj = Entity(model = 'quad', position = (30, 105, -0.13), scale = (7, 7, 0), texture = tent_texture, tag = 1)
    church_obj = Entity(model = 'quad', position = (80, 185, -0.13), scale = (22, 22, 0), texture = church_texture, tag = 1)

    player.building_layers_list = [tent_obj, church_obj]

    '''
    general_store = Entity(model='plane',
                           position=(22, 2, 0),
                           scale=(16, 0, -9),
                           texture='textures\\buildings\\city_station',
                           rotation=(90, 0, 0),
                           )

    sheriff = Entity(model='plane',
                     position=(32, 2, 0),
                     scale=(16, 0, -9),
                     texture='textures\\buildings\\fisher',
                     rotation=(90, 0, 0),
                     )'''

