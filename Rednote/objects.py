
# REDNOTE - OBJECTS
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] #

from ursina import *

saloon_texture = 'textures/buildings/saloon.png'

def place_all_objects():
    print('befogom a pofámat')

    bank = Entity(model = 'quad',
                  position = (50, -15, -0.1),
                  scale = (25, 16.5, 0),
                  texture = 'textures/buildings/rustfort_bank',
                  rotation = (0, 0, 0),
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

