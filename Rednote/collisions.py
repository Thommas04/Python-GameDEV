from ursina import *


def townlevel_collision():
    global coll_list

    col_z = 0.5 # collision_z -> megadja a collision melyseget z tengelyen.

    coll_list = []

    tcds = ( ((1,1,0),(4,2,0)), # townlevel_collision_dots
             ((17.64, 3.32, 0),(27.61, -0.1, 0)),
             ((16.98, -0.16, 0),(22.1, -0.54, 0)),
             ((55.54, 14.66, 0),(17.14, 9.7, 0)),
             ((31.35, -0.17, 0),(32.09, -0.47, 0))

           )

    for i in tcds:
        pos_x = ((i[1][0] - i[0][0]) / 2) + i[0][0]
        pos_y = ((i[1][1] - i[0][1]) / 2) + i[0][1]
        scale_x = abs(i[0][0] - i[1][0])
        scale_y = abs(i[0][1] - i[1][1])

        print('gecii:', pos_x, pos_y)
        coll_list.append(Entity(model='cube', collider='mesh', position=(pos_x, pos_y, col_z), scale=(scale_x, scale_y, 0.5), color=color.azure))
