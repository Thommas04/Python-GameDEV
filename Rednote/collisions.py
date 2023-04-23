from ursina import *


def townlevel_collision():
    col_z = -0.1 # collision_z -> megadja a collision melyseget z tengelyen.

    collision_list= []
    building_collision_list = []
    water_surface_list = []

    tcds = [[(0,113),(19,109)], [(18, 118), (19, 113)], [(19,118),(40,114)], [(40,117),(48,114)], [(48, 118), (56, 114)], [(56, 117), (57, 114)], [(57, 116), (58, 114)], [(58,115),(59,114)], [(20, 114), (23, 113)], [(42, 114), (47, 113)], [(53, 153), (60, 122)], [(55, 122), (60, 121)], [(50, 195), (53, 149)], [(51, 149), (53, 148)], [(48, 200), (50, 190)], [(60, 141), (61, 139)], [(61, 142), (63, 140)], [(63, 143), (65, 141)], [(65, 147), (67, 142)], [(67, 147), (88, 146)], [(87, 146), (89, 145)], [(88, 145), (90, 144)], [(89, 144), (103, 143)], [(102, 163), (103, 144)], [(96, 163), (102, 162)], [(96, 162), (97, 157)], [(72, 158), (96, 157)], [(72, 168), (73, 158)], [(71, 168), (72, 167)], [(70, 169), (71, 167)], [(67, 170), (70, 169)], [(65, 171), (67, 169)], [(65, 193), (66, 171)], [(66, 194), (69, 192)], [(69, 194), (78, 193)], [(77, 195), (83, 194)], [(82, 196), (86, 195)], [(85, 195), (90, 194)], [(90, 194), (91, 193)], [(92, 200), (94, 193)], [(90, 196), (91, 194)], [(91, 196), (92, 195)], [(94, 200), (97, 198)], [(112, 200), (160, 194)], [(159, 194), (163, 189)], [(163, 191), (168, 190)], [(167, 190), (175, 189)], [(174, 191), (185, 190)], [(184, 192), (190, 191)], [(189, 191), (195, 190)], [(194, 190), (200, 186)], [(176, 190), (177, 179)], [(172, 179), (177, 175)], [(172, 175), (173, 159)], [(171, 159), (173, 155)], [(170, 159), (171, 154)], [(169, 158), (170, 154)], [(168, 158), (169, 153)], [(167, 156), (168, 146)], [(161, 150), (167, 146)], [(155, 151), (161, 147)], [(155, 147), (156, 146)], [(160, 147), (161, 146)], [(146, 150), (155, 146)], [(146, 154), (147, 150)], [(144, 159), (145, 151)], [(145, 155), (146, 151)], [(109, 153), (111, 152)], [(109, 152), (110, 145)], [(110, 149), (111, 145)], [(111, 150), (112, 145)], [(112, 150), (116, 146)], [(115, 151), (118, 147)], [(118, 155), (119, 148)], [(117, 152), (118, 151)], [(122, 156), (124, 155)], [(122, 155), (123, 149)], [(117, 155), (118, 154)], [(123, 153), (128, 149)], [(128, 152), (134, 149)], [(134, 153), (139, 148)], [(138, 148), (139, 128)], [(139, 132), (140, 128)], [(140, 131), (161, 127)], [(160, 130), (165, 126)], [(165, 129), (166, 126)], [(166, 128), (167, 126)], [(167, 127), (168, 126)], [(111, 175), (113, 174)], [(111, 174), (112, 168)], [(112, 172), (115, 168)], [(114, 173), (120, 169)], [(117, 169), (121, 168)], [(120, 172), (123, 168)], [(122, 179), (123, 172)], [(121, 179), (122, 178)], [(71, 109), (72, 81)], [(72, 85), (73, 81)], [(73, 83), (80, 79)], [(79, 79), (80, 73)], [(80, 77), (99, 73)], [(98, 78), (101, 74)], [(100, 79), (103, 75)], [(102, 80), (105, 76)], [(104, 81), (134, 77)], [(107, 82), (113, 81)], [(133, 84), (134, 81)], [(136, 84), (137, 77)], [(137, 81), (141, 77)], [(140, 80), (159, 76)], [(158, 79), (163, 75)], [(162, 78), (171, 74)], [(170, 77), (176, 73)], [(176, 76), (177, 73)], [(177, 75), (178, 73)], [(178, 74), (179, 73)], [(175, 87), (177, 86)], [(175, 86), (176, 80)], [(176, 84), (177, 80)], [(177, 84), (178, 79)], [(178, 83), (179, 79)], [(179, 83), (180, 78)], [(180, 82), (181, 78)], [(181, 82), (182, 77)], [(182, 81), (184, 77)], [(183, 77), (184, 65)], [(184, 69), (187, 65)], [(186, 65), (187, 58)], [(187, 63), (189, 58)], [(188, 58), (189, 44)], [(189, 45), (190, 43)], [(190, 44), (191, 42)], [(191, 43), (192, 41)], [(192, 42), (193, 40)], [(193, 41), (198, 39)], [(195, 37), (199, 36)], [(197, 36), (200, 35)], [(198, 35), (200, 29)], [(148, 76), (151, 75)], [(168, 74), (170, 73)], [(174, 73), (176, 72)], [(83, 146), (85, 145)], [(98, 143), (100, 142)], [(123, 149), (125, 148)], [(6, 195), (30, 193)], [(29, 197), (30, 194)], [(30, 197), (48, 195)], [(0, 34), (1, 26)], [(1, 35), (2, 33)], [(2, 36), (3, 34)], [(3, 37), (4, 35)], [(4, 37), (6, 36)], [(3, 40), (8, 39)], [(7, 52), (10, 40)], [(3, 39), (4, 37)], [(6, 52), (8, 51)], [(5, 62), (6, 51)], [(6, 53), (7, 52)], [(0, 62), (5, 61)], [(198, 40), (199, 37)], [(192, 163), (200, 150)], [(191, 150), (200, 142)], [(189, 142), (200, 128)], [(190, 128), (200, 114)], [(193, 114), (200, 100)], [(194, 100), (200, 95)], [(195, 95), (200, 75)], [(196, 75), (200, 74)], [(194, 164), (200, 163)], [(196, 165), (200, 164)], [(64,71),(65,61)], [(68,71),(69,61)], [(166,40),(176,39)], [(166,37),(176,36)], [(6,123),(14,122)], [(6,126),(14,125)], [(139, 194), (142, 193)], [(155, 194), (158, 193)],

            ]



    water_surface = [ [(18,185),(24,180)], [(24,182),(27,178)], [(27, 181), (28, 178)], [(10, 180), (25, 172)], [(25, 178), (26, 177)], [(10, 181), (18, 180)], [(12, 182), (18, 181)], [(13, 183), (18, 182)], [(16, 184), (18, 183)], [(25, 175), (26, 172)], [(26, 174), (28, 169)], [(11, 172), (27, 169)], [(11, 169), (23, 168)], [(11, 168), (18, 167)], [(11, 167), (17, 165)], [(9, 179), (10, 174)], [(10, 166), (16, 159)], [(9, 163), (15, 133)], [(7, 120), (13, 113)], [(6, 122), (14, 120)], [(13, 120), (14, 119)], [(7, 109), (13, 103)], [(8, 103), (13, 99)], [(9, 98), (13, 95)], [(9, 95), (14, 92)], [(7, 93), (14, 88)], [(6, 89), (15, 86)], [(9, 98), (13, 95)], [(9, 95), (14, 92)], [(7, 93), (14, 88)], [(6, 89), (15, 86)], [(9, 99), (13, 98)], [(6, 130), (14, 126)], [(7, 135), (14, 130)], [(8, 144), (9, 135)], [(0, 82), (4, 78)], [(1, 83), (7, 79)], [(3, 84), (15, 80)], [(7, 86), (15, 84)], [(15, 82), (16, 80)], [(9, 80), (17, 76)], [(17, 78), (18, 76)], [(10, 76), (18, 74)], [(11, 74), (22, 72)], [(18, 75), (19, 74)], [(12, 72), (23, 71)], [(13, 71), (25, 70)], [(14, 70), (25, 68)], [(17, 69), (28, 67)], [(18, 67), (31, 66)], [(25, 69), (28, 68)], [(19, 66), (31, 64)], [(20, 64), (38, 62)], [(32, 65), (34, 64)], [(24, 62), (37, 60)], [(28, 60), (37, 59)], [(29, 59), (37, 58)], [(32, 58), (37, 57)], [(33, 57), (37, 56)], [(36, 56), (44, 55)], [(38, 63), (47, 56)], [(28, 68), (29, 67)], [(31, 65), (32, 64)], [(37, 62), (38, 56)], [(45, 64), (47, 63)], [(46, 65), (47, 64)], [(47, 65), (53, 58)], [(47, 58), (51, 57)], [(48, 66), (53, 65)], [(52, 67), (53, 66)], [(53, 67), (58, 60)], [(55, 68), (58, 67)], [(58, 69), (64, 63)], [(58, 63), (62, 61)], [(62, 63), (63, 62)], [(69, 69), (80, 63)], [(72, 63), (80, 62)], [(78, 62), (80, 61)], [(80, 68), (89, 61)], [(84, 61), (98, 60)], [(89, 67), (99, 61)], [(99, 67), (104, 62)], [(100, 68), (104, 67)], [(102, 70), (104, 68)], [(104, 71), (106, 63)], [(106, 71), (109, 64)], [(109, 72), (110, 65)], [(110, 72), (124, 66)], [(113, 73), (124, 72)], [(53, 60), (54, 59)], [(124, 72), (128, 65)], [(125, 65), (128, 64)], [(128, 71), (135, 64)], [(130, 64), (135, 63)], [(135, 70), (138, 63)], [(138, 70), (142, 64)], [(141, 71), (148, 65)], [(148, 70), (160, 65)], [(149, 65), (160, 64)], [(150, 64), (160, 63)], [(160, 69), (169, 63)], [(169, 68), (172, 63)], [(172, 3), (180, 0)], [(180, 3), (181, 2)], [(171, 12), (179, 3)], [(179, 10), (181, 3)], [(169, 12), (171, 10)], [(170, 10), (171, 9)], [(169, 16), (177, 12)], [(167, 16), (169, 15)], [(168, 15), (169, 14)], [(167, 23), (175, 16)], [(166, 27), (175, 23)], [(165, 33), (166, 26)], [(166, 45), (176, 40)], [(167, 49), (177, 45)], [(176, 45), (177, 42)], [(177, 45), (178, 43)], [(168, 55), (176, 49)], [(168, 57), (177, 55)], [(173, 62), (176, 57)], [(177, 48), (178, 45)], [(176, 60), (177, 57)], [(161, 63), (165, 62)], [(164, 62), (165, 61)], [(165, 63), (173, 58)], [(167, 58), (173, 57)], [(173, 64), (174, 62)], [(172, 66), (173, 63)], [(166, 36), (174, 27)], [(173, 36), (176, 32)], [(174, 32), (175, 31)], [(170, 111), (185, 105)], [(185, 109), (186, 105)], [(171, 105), (187, 102)], [(172, 102), (187, 101)], [(182, 101), (187, 96)], [(173, 96), (187, 92)], [(174, 92), (178, 91)], [(178, 92), (187, 90)], [(185, 90), (189, 89)], [(173, 112), (185, 111)], [(176, 113), (182, 112)], [(172, 101), (179, 96)], [(179, 100), (180, 96)], [(180, 98), (182, 96)], [(187, 96), (188, 90)], [(188, 95), (189, 90)],

                      ]

    buildings = [[(0, 0),(-1, 200)],
                 [(0, 0), (200, -1)],
                 [(200, 200), (201, 0)],
                 [(0, 201), (200, 200)],
                 [(116,104.3),(131.4,99)], # sherrif
                 [(116,99),(122,98)],
                 [(125, 99), (131.4, 98)],

                 [(150, 103), (164, 99)], # bank
                 [(151, 99), (156, 98)],
                 [(158, 99), (164, 98)],

                 [(122.4, 125), (136.4, 118)], # saloon
                 [(122.4, 118), (129, 117)],
                 [(130.5, 118), (136.4, 117)],

                 [(123, 147), (137, 142)], # house 1
                 [(123, 142), (129, 141)],
                 [(132, 142), (137, 141)],

                 [(75, 190), (89, 185)], # church
                 [(75, 185), (81, 184)],
                 [(83, 185), (86, 183)],
                 [(83, 183), (84, 182)],
                 [(78, 185), (81, 183)],
                 [(80, 183), (81, 182)],
                 [(81, 185), (83, 184)],

                 [(33.5, 195), (48, 189)],
                 [(33.5, 189), (37, 187)], # house 2
                 [(39, 189), (42, 187)],

                 [(67, 147), (83.6, 140.4)], # shop
                 [(81, 141), (83, 140)],

                 [(95.5, 37.4), (110, 31)], # train station
                 [(95.5, 32), (101, 30)],
                 [(96, 32), (101, 30)],
                 [(100, 30), (101, 29)],
                 [(104, 32), (109, 30)],
                 [(104, 30), (105, 29)],

                 [(32, 100.4), (37, 99)], # tent
                 [(31, 99), (33, 97)],
                 [(35, 99), (37, 97)],
                 [(33, 99), (35, 98)],

                 ]



    for building_points in buildings:
        building_collision_list.append(Entity(model='quad', collider='box', tag = 'building_collision', origin = (-0.5,0.5), position=(building_points[0][0], building_points[0][1], col_z), scale=(building_points[1][0]-building_points[0][0], building_points[0][1]-building_points[1][1], 0.5), color=color.pink))

    for points in tcds:
        collision_list.append(Entity(model='quad', collider='box', tag = 'terrain_collision', origin = (-0.5,0.5), position=(points[0][0], points[0][1], col_z), scale=(points[1][0]-points[0][0], points[0][1]-points[1][1], 0.5), color=color.azure))

    for water_surfacee in water_surface:
        water_surface_list.append(Entity(model='quad', collider='box', tag = 'water_surface', origin = (-0.5,0.5), position=(water_surfacee[0][0], water_surfacee[0][1], col_z), scale=(water_surfacee[1][0]-water_surfacee[0][0], water_surfacee[0][1]-water_surfacee[1][1], 0.5), color=color.red))

    for i in collision_list:
        i.alpha = 0
    for i in building_collision_list:
        i.alpha = 0
    for i in water_surface_list:
        i.alpha = 0

    return collision_list