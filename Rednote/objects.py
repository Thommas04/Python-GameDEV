
from ursina import *

def place_all_objects():
    saloon = Entity(model='plane',
                    position=(10, 2, 0),
                    scale=(16, 0, -9),
                    texture='textures\\buildings\\saloon',
                    rotation=(90, 0, 0),
                    )

    bank = Entity(model='plane',
                  position=(-100, 2, 0),
                  scale=(16, 0, -9),
                  texture='textures\\buildings\\rustfort_bank',
                  rotation=(90, 0, 0),
                  )

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
                     )

    bigbox = Entity(model='plane',
                    position=(0, 0, 0.005),
                    scale=(200,0,-200),
                    texture='textures\\misc\\background',
                    rotation=(90, 0, 0),
                    collider = 'box'
                    )
