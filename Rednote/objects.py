
# REDNOTE - OBJECTS
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] #

from ursina import *

saloon_texture = 'textures/buildings/saloon.png'

def place_all_objects():
    print('befogom a pofámat')

    saloon = Entity(model = 'cube',
                    position = (35, 2, -0.05),
                    scale = (16, 0, -9),
                    texture = saloon_texture,
                    rotation = (90, 0, 0),
                    doublesided = True
                    )

    bank = Entity(model = 'cube',
                  position = (20, -5, -0.05),
                  scale = (48, 0, -27),
                  texture = 'textures\\buildings\\rustfort_bank',
                  rotation = (90, 0, 0),
                  doublesided = True
                  )
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

