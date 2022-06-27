
# URSINA IMPORTS
from ursina import *
from ursina.shaders import lit_with_shadows_shader

# Own modules
from time import sleep
from functions import *
from player import *
from objects import *
from anims import *

app = Ursina()

EditorCamera()
#create_net() # keszit egy halot


# ---------------------------------------------------------------------------------------------------------------------[]
# [ KeyBINDS ]---------------------------------------------------------------------------------------------------------[]

runBIND = "shift"

move_upBIND = "w"
move_downBIND = "s"
move_leftBIND = "a"
move_rightBIND = "d"

# ---------------------------------------------------------------------------------------------------------------------[]
# [ Variables ]--------------------------------------------------------------------------------------------------------[]

# camera :
camera.fov = 60 # default [ field of view ]

camera_maxheight = 100 # A kamera es a karakter mozgato WASD-vel - ez adja meg a vegso hatarerteket magassagban.
camera_maxwidth = 100

walkspeed = 5 # A karakter es a kamera mozgasi sebessege, WASD-vel.
runspeed = 10 # Ezt a mennyiseget adja hozza a jatekos walkspeedjehez.

player_scale = (1.2, 0, -1.67)

# [ END Variables ]----------------------------------------------------------------------------------------------------[]
# ---------------------------------------------------------------------------------------------------------------------[]
# [Declare Objects]----------------------------------------------------------------------------------------------------[]


verts = ((17.22, -0.14, 0),
(18.6, -0.21, 0),
(17.54, 3.24, 0),
(17.54, 3.26, 0),
(18.74, -0.46, 0),
(22.03, -0.48, 0),
(22.03, -0.46, 0),
(21.85, 3.21, 0),
(17.54, 3.26, 0),
(21.85, 3.21, 0),
(22.05, -0.17, 0),
(27.15, -0.21, 0),
(27.15, -0.21, 0),
(21.85, 3.21, 0),
(26.36, 3.1, 0),
(21.85, 3.14, 0),
(27.11, -0.18, 0),
(26.58, 3.16, 0))
tris = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)

e = Entity(model=Mesh(vertices=verts, triangles=tris), scale = 1)


upper_body = Entity(model = 'plane',
                    position = Vec3(0, 0, -0.5),
                    scale = player_scale,
                    rotation = (90, 0, 0),
                    collider = 'mesh',
                    texture = 'textures\\main_character\\front_view\\upper_body\\front_anim_up1'
                    )

lower_body = Entity(model = 'plane',
                    position = Vec3(0, 0.005, -0.4),
                    scale = player_scale,
                    rotation = (90, 0, 0),
                    collider = 'mesh',
                    texture = 'textures\\main_character\\front_view\\lower_body\\front_anim1'
                    )

# [ Lights ]-----------------------------------------------------------------------------------------------------------[]

#L1 = PointLight(y = -2, z = 100, color = color.black, scale = 1000)
#L2 = PointLight(y = -5, z = 100, color = color.blue, scale = 1000)
#L3 = PointLight(y = -5, z = 10, color = color.blue, scale = 100)

# [ Functions ]--------------------------------------------------------------------------------------------------------[]

refresh = True
def anim_loop(): # ez gyakorlatilag egy folyamatos rekurziv loop, ami az animaciokat vezerli framekent.
    global refresh
    refresh = not refresh

    invoke(Func(front_anim, refresh, upper_body, lower_body), delay=0)

    if held_keys[runBIND]:
        invoke(anim_loop, delay = 0.02)
    else:
        invoke(anim_loop, delay = 0.035)
anim_loop()

place_all_objects() # lerakja az osszes modelt a fajlbol

# [ Update Function ]--------------------------------------------------------------------------------------------------[]

player_body_part = [upper_body, lower_body]


def update():
    global movespeed

    if held_keys[runBIND]:
        movespeed = walkspeed + runspeed # A movespeed egyenlo a jatekos es a kamera sebessegevel
    else:
        movespeed = walkspeed # kivonja a futasi sebesseg ereteket.

    camera_control(player_body_part, camera_maxheight, camera_maxwidth, move_upBIND, move_downBIND, move_rightBIND, move_leftBIND, movespeed)

# []-------------------------------------------------------------------------------------------------------------------[]

app.run()
