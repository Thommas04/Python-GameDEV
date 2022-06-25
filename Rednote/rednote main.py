
# URSINA IMPORTS
from ursina import *
from ursina.shaders import lit_with_shadows_shader

# Own modules
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

class Player:
    def __init__(self):
        global player_body, player_right_upper_leg, player_right_lower_leg, player_right_upper_arm, player_right_lower_arm
        global player_left_upper_leg, player_left_lower_leg, player_left_upper_arm, player_left_lower_arm
        player_body = Entity(model = 'plane',
                            position = Vec3(0, 0, -0.5),
                            scale = player_scale,
                            rotation = (90, 0, 0),
                            collider = 'mesh',
                            texture = 'textures\\main_character\\front_view\\front-body'
                            )

        player_right_upper_leg = Entity(model = 'plane',
                            position = Vec3(0, 0, -0.5),
                            scale = player_scale,
                            rotation = (90, 0, 0),
                            collider = 'mesh',
                            texture = 'textures\\main_character\\front_view\\front-right_leg'
                            )

        player_right_lower_leg = Entity(model = 'plane',
                            position = (0, 0, -0.5),
                            scale = player_scale,
                            rotation = Vec3(90, 0, 0),
                            collider = 'mesh',
                            texture = 'textures\\misc\\transparent'
                            )

        player_right_upper_arm = Entity(model = 'plane',
                            position = (0, 0, -0.5),
                            scale = player_scale,
                            rotation = (90, -20, 20),
                            collider = 'mesh',
                            texture = 'textures\\main_character\\front_view\\front-right_arm'
                            )

        player_right_lower_arm = Entity(model = 'plane',
                            position = (0, 0, -0.5),
                            scale = player_scale,
                            rotation = (90, 0, 0),
                            collider = 'mesh',
                            texture = 'textures\\misc\\transparent'
                            )

        player_left_upper_leg = Entity(model = 'plane',
                            position = (0, 0, -0.5),
                            scale = player_scale,
                            rotation = (90, 0, 0),
                            collider = 'mesh',
                            texture = 'textures\\main_character\\front_view\\front-left_leg'
                            )

        player_left_lower_leg = Entity(model = 'plane',
                            position = (0, 0, -0.5),
                            scale = player_scale,
                            rotation = (90, 0, 0),
                            collider = 'mesh',
                            texture = 'textures\\misc\\transparent'
                            )

        player_left_upper_arm = Entity(model = 'plane',
                            position = (0, 0, -0.5),
                            scale = player_scale,
                            rotation = (90, 0, 0),
                            collider = 'mesh',
                            texture = 'textures\\main_character\\front_view\\front-left_arm'
                            )

        player_left_lower_arm = Entity(model = 'plane',
                            position = (0, 0, -0.5),
                            scale = player_scale,
                            rotation = (90, 0, 0),
                            collider = 'mesh',
                            texture = 'textures\\misc\\transparent'
                            )




    def move_right(self):
        print("yes")

main_character = Player()

# [ Lights ]-----------------------------------------------------------------------------------------------------------[]

#L1 = PointLight(y = -2, z = 100, color = color.black, scale = 1000)
#L2 = PointLight(y = -5, z = 100, color = color.blue, scale = 1000)
#L3 = PointLight(y = -5, z = 10, color = color.blue, scale = 100)

# [ Functions ]--------------------------------------------------------------------------------------------------------[]

place_all_objects() # lerakja az osszes modelt a fajlbol

# [ Update Function ]--------------------------------------------------------------------------------------------------[]

player_body_part = [player_body, player_body, player_right_upper_leg, player_right_lower_leg, player_right_upper_arm, player_right_lower_arm,
                    player_left_upper_leg, player_left_lower_leg, player_left_upper_arm, player_left_lower_arm]

def front_anim():
    if held_keys['s']:
        invoke(Func(front_anims_forward, player_right_upper_arm, player_left_upper_arm, player_right_upper_leg,
                    player_left_upper_leg), delay=0.2)
        invoke(Func(front_anims_backward, player_right_upper_arm, player_left_upper_arm, player_right_upper_leg,
                    player_left_upper_leg), delay=0.2)


    else:
        player_right_upper_arm.animate('rotation_x', 80, duration=2, delay=-0.2, curve=curve.linear)
        player_left_upper_arm.animate('rotation_x', 80, duration=2, delay=-0.2, curve=curve.linear)
        player_right_upper_leg.animate('rotation_x', 80, duration=2, delay=-0.2, curve=curve.linear)
        player_left_upper_leg.animate('rotation_x', 80, duration=2, delay=-0.2, curve=curve.linear)

def update():
    global movespeed

    invoke(front_anim, delay = 0.5)

    if held_keys[runBIND]:
        movespeed = walkspeed + runspeed # A movespeed egyenlo a jatekos es a kamera sebessegevel
    else:
        movespeed = walkspeed # kivonja a futasi sebesseg ereteket.

    camera_control(player_body_part, camera_maxheight, camera_maxwidth, move_upBIND, move_downBIND, move_rightBIND, move_leftBIND, movespeed)

# []-------------------------------------------------------------------------------------------------------------------[]

app.run()
