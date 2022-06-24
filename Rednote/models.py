
from ursina import *

def place_all_objects():
    player = Entity(model='cube',
                    position=(0, 0, 0),
                    scale=(0.5),
                    rotation=(90, 0, 0),
                    collider='mesh'
                    )

    saloon = Entity(model='plane',
                    position=(10, 2, 0),
                    scale=(16, 0, -9),
                    texture='textures\\buildings\\saloon',
                    rotation=(90, 0, 0),
                    collider='mesh'
                    )

    bank = Entity(model='plane',
                  position=(-5, 2, 0),
                  scale=(16, 0, -9),
                  texture='textures\\buildings\\rustfort_bank',
                  rotation=(90, 0, 0),
                  collider='mesh'
                  )

    general_store = Entity(model='plane',
                           position=(22, 2, 0),
                           scale=(16, 0, -9),
                           texture='textures\\buildings\\city_station',
                           rotation=(90, 0, 0),
                           collider='mesh'
                           )

    sheriff = Entity(model='plane',
                     position=(32, 2, 0),
                     scale=(16, 0, -9),
                     texture='textures\\buildings\\fisher',
                     rotation=(90, 0, 0),
                     collider='mesh'
                     )