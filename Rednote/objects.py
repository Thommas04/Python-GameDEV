
# REDNOTE - OBJECTS
# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][] #

from ursina import *
from daylight_cycle import LightSource

#OBJECT Textures for Interactives
lamp_post_sheet = 'textures/objects/lights/lamp_posts_sheet.png'

#TEXTURES
tent_texture = 'textures/buildings/summer/tent.png'
church_texture = 'textures/buildings/summer/church.png'
bank_texture = 'textures/buildings/summer/bank.png'
saloon_texture = 'textures/buildings/summer/saloon.png'
saloon_texture_extended = 'textures/buildings/summer/saloon_extended.png'
sheriff_texture = 'textures/buildings/summer/sheriff.png'
train_station_texture = 'textures/buildings/summer/train_station.png'
shop_texture = 'textures/buildings/summer/shop.png'

house1_texture = 'textures/buildings/summer/house_1.png'
house2_texture = 'textures/buildings/summer/house_2.png'

static_z_axis = -0.18
z_axis_hovered = -0.16
z_axis_lowered = -0.12

class InteractiveObject(Entity):
    def __init__(self, player, x, y, tag, scale = (1, 1, 0), lit = False):
        self.tag = tag

        x += 0.5
        y -= 1

        if tag == 'lamp_post':
            self.object = Entity(tag = tag, texture = lamp_post_sheet, model = 'quad', position = (x, y, -0.5), origin = (0,-0.5), scale = (1.2, 5.2, 0), alpha = 1, tileset_size = [2,1], tile_coordinate = [0,0])
            self.light = LightSource(host = player, position = [x, y + 3.5], type = 'street_lamp', color = color.yellow)
            self.collision = Entity(model='quad', collider='box', position=(x, y, -0.1), scale=(1.2,1,0.1), alpha = 0, tag = 'interactive_object_collision')


            if lit == True:
                self.object.tile_coordinate = [0,0]
            else:
                self.object.tile_coordinate = [1,0]


        player.interactive_object_list.append(self)







# ----------------------------------------------------------------------------------------------------------------------

def place_buildings(player):

    tent_obj_floor = Entity(model = 'quad', position = (34, 98.52, -0.1), scale = (7, 3.5, 0), texture = tent_texture, tileset_size = [1,2], tile_coordinate = [0,0])
    tent_obj_roof = Entity(model='quad', position=(34, 102, -0.7), scale=(7, 3.5, 0), texture=tent_texture, tileset_size = [1,2], tile_coordinate = [0,1])

    church_obj_floor = Entity(model = 'quad', position = (82, 184.1, -0.1), scale = (22, 11, 0), texture = church_texture, tileset_size = [1,2], tile_coordinate = [0,0])
    church_obj_roof = Entity(model = 'quad', position = (82, 195, -0.7), scale = (22, 11, 0), texture = church_texture, tileset_size = [1,2], tile_coordinate = [0,1])

    saloon_obj_floor = Entity(model = 'quad', position = (128.8,118.9, -0.1), scale = (24, 12, 0), texture = saloon_texture, tileset_size = [1,2], tile_coordinate = [0,0])
    saloon_obj_roof = Entity(model = 'quad', position = (128.8,130.8, -0.7), scale = (24, 12, 0), texture = saloon_texture, tileset_size = [1,2], tile_coordinate = [0,1])
    saloon_obj_tree = Entity(model = 'quad', position = (128.8,126.8, -0.7), scale = (24, 24, 0), texture = saloon_texture_extended)

    sheriff_obj_floor = Entity(model = 'quad', position = (123.9,100.8, -0.1), scale = (18, 7, 0), texture = sheriff_texture, tileset_size = [1,2], tile_coordinate = [0,0])
    sheriff_obj_roof = Entity(model='quad', position=(123.9, 107.7, -0.7), scale=(18, 7, 0), texture=sheriff_texture, tileset_size=[1, 2], tile_coordinate=[0, 1])

    bank_obj_floor = Entity(model = 'quad', position = (157.0,98.8, -0.1), scale = (16, 8, 0), texture = bank_texture, tileset_size = [1,2], tile_coordinate = [0,0])
    bank_obj_roof = Entity(model = 'quad', position = (157.0,106.7, -0.7), scale = (16, 8, 0), texture = bank_texture, tileset_size = [1,2], tile_coordinate = [0,1])

    house2_obj_floor = Entity(model = 'quad', position = (40.7,190.4, -0.1), scale = (16, 8, 0), texture = house2_texture, tileset_size = [1,2], tile_coordinate = [0,0])
    house2_obj_roof = Entity(model = 'quad', position = (40.7,198.3, -0.7), scale = (16, 8, 0), texture = house2_texture, tileset_size = [1,2], tile_coordinate = [0,1])

    house1_obj_floor = Entity(model = 'quad', position = (130.2,143.2, -0.1), scale = (15, 7.5, 0), texture = house1_texture, tileset_size = [1,2], tile_coordinate = [0,0])
    house1_obj_roof = Entity(model = 'quad', position = (130.2,150.6, -0.7), scale = (15, 7.5, 0), texture = house1_texture, tileset_size = [1,2], tile_coordinate = [0,1])

    shop_obj_floor = Entity(model = 'quad', position = (75.1,142.9, -0.1), scale = (20, 10, 0), texture = shop_texture, tileset_size = [1,2], tile_coordinate = [0,0])
    shop_obj_roof = Entity(model = 'quad', position = (75.1,152.8, -0.7), scale = (20, 10, 0), texture = shop_texture, tileset_size = [1,2], tile_coordinate = [0,1])

    train_station_obj_floor = Entity(model = 'quad', position = (102.5,33.2, -0.1), scale = (17, 8.5, 0), texture = train_station_texture, tileset_size = [1,2], tile_coordinate = [0,0])
    train_station_obj_roof = Entity(model = 'quad', position = (102.5,41.6, -0.7), scale = (17, 8.5, 0), texture = train_station_texture, tileset_size = [1,2], tile_coordinate = [0,1])


