from ursina import *


def townlevel_collision():
    col_z = -0.1 # collision_z -> megadja a collision melyseget z tengelyen.

    collision_list= []
    building_collision_list = []

    tcds = [
            ]

    buildings = [
                 ]


    for building_points in buildings:
        building_collision_list.append(Entity(model='quad', collider='box', tag = 'building_collision', origin = (-0.5,0.5), position=(building_points[0][0], building_points[0][1], col_z), scale=(building_points[1][0]-building_points[0][0], building_points[0][1]-building_points[1][1], 0.5), color=color.pink))


    for points in tcds:
        collision_list.append(Entity(model='quad', collider='box', tag = 'terrain_collision', origin = (-0.5,0.5), position=(points[0][0], points[0][1], col_z), scale=(points[1][0]-points[0][0], points[0][1]-points[1][1], 0.5), color=color.azure))

    for i in collision_list:
        i.alpha = 0
    for i in building_collision_list:
        i.alpha = 0

    return collision_list