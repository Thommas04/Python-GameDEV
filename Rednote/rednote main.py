
# URSINA IMPORTS
from ursina import *
from ursina.shaders import lit_with_shadows_shader

# Own modules
from time import sleep
from functions import *
from camera_control import *
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
camera.fov = 43.62 # default [ field of view ]

camera_maxheight = 100 # A kamera es a karakter mozgato WASD-vel - ez adja meg a vegso hatarerteket magassagban.
camera_maxwidth = 100

walkspeed = 5 # A karakter es a kamera mozgasi sebessege, WASD-vel.
runspeed = 10 # Ezt a mennyiseget adja hozza a jatekos walkspeedjehez.

player_scale = (1.2, 0, -1.67)

# [ END Variables ]----------------------------------------------------------------------------------------------------[]
# ---------------------------------------------------------------------------------------------------------------------[]
# [Declare Objects]----------------------------------------------------------------------------------------------------[]


verts = ((0,0,0), (1,0,0), (.5, 1, 0), (-.5,1,0))
tris = (1, 2, 0, 2, 3, 0)

#e = Entity(model=Mesh(vertices=verts, triangles=tris), scale=2)


upper_body = Entity(model = 'plane',
                    position = Vec3(0, 0, -0.5),
                    scale = player_scale,
                    rotation = (90, 0, 0),
                    collider = 'mesh',
                    texture = 'textures\\main_character\\front_view\\upper_body\\front_anim_up1'
                    )

lower_body = Entity(model = 'plane',
                    position = Vec3(0, 0.001, -0.5),
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

    invoke(anim_loop, delay = 0.04 )
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
