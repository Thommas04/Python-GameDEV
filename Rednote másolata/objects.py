
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

        if tag == 'lamp_post':
            self.object = Entity(tag = tag, texture = lamp_post_sheet, model = 'quad', position = (x, y - 0.4, -0.13), origin = (0,-0.5), scale = (1.2, 5.2, 0), alpha = 1, tileset_size = [2,1], tile_coordinate = [0,0])
            self.light = LightSource(host = player, position = [x, y + 3.5], type = 'street_lamp', color = color.yellow)
            self.collision = Entity(model='quad', collider='box', position=(x, y, -0.1), scale=(1.2,1,0.1), alpha = 0, tag = 'interactive_object_collision')

            if lit == True:
                self.object.tile_coordinate = [0,0]
            else:
                self.object.tile_coordinate = [1,0]


        player.interactive_object_list.append(self)







# ----------------------------------------------------------------------------------------------------------------------

def place_buildings(player):

    tent_obj = Entity(model = 'quad', position = (30, 105, -0.13), scale = (7, 7, 0), texture = tent_texture, tag = [0, 6])
    church_obj = Entity(model = 'quad', position = (80, 185, -0.13), scale = (22, 22, 0), texture = church_texture, tag = [0, 12])
    saloon_obj = Entity(model = 'quad', position = (124.8,127.8, -0.13), scale = (24, 24, 0), texture = saloon_texture, tag = [-6, 13])
    sheriff_obj = Entity(model = 'quad', position = (119.9,107.8, -0.13), scale = (18, 14, 0), texture = sheriff_texture, tag = [-2, 11])
    bank_obj = Entity(model = 'quad', position = (153.0,105.7, -0.13), scale = (16, 16, 0), texture = bank_texture, tag = [0, 12])
    house2_obj = Entity(model = 'quad', position = (36.7,193.3, -0.13), scale = (16, 16, 0), texture = house2_texture, tag = [0, 12])
    house1_obj = Entity(model = 'quad', position = (126.2,147.6, -0.13), scale = (15, 15, 0), texture = house1_texture, tag = [0, 12])
    shop_obj = Entity(model = 'quad', position = (74.1,146.8, -0.13), scale = (20, 20, 0), texture = shop_texture, tag = [0, 12])
    train_station_obj = Entity(model = 'quad', position = (98.5,40.6, -0.13), scale = (17, 17, 0), texture = train_station_texture, tag = [-1, 12])


    player.building_layers_list = [tent_obj, church_obj, saloon_obj, sheriff_obj, bank_obj, house1_obj, house2_obj, shop_obj, train_station_obj]

