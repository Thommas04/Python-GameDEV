
# URSINA IMPORTS
from ursina import *
from ursina.shaders import lit_with_shadows_shader


from functions import *
from camera_control import *

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


# [ END Variables ]----------------------------------------------------------------------------------------------------[]
# ---------------------------------------------------------------------------------------------------------------------[]
# [Declare Objects]----------------------------------------------------------------------------------------------------[]

map = Entity(model = 'cube',
             position = (0, 0, 0.01),
             scale = (16, 0, -9),
             texture = 'textures\\teszt',
             rotation = (90,0,0)
            )

verts = ((0,0,0), (1,0,0), (.5, 1, 0), (-.5,1,0))
tris = (1, 2, 0, 2, 3, 0)

e = Entity(model=Mesh(vertices=verts, triangles=tris), scale=2)

player = Entity(model = 'cube',
             position = (0, 0, 0),
             scale = (0.5),
             rotation = (90,0,0),
             collider = 'mesh'
            )

box = Entity(model = 'plane',
             position = (10, 2, 0),
             scale = (16, 0, -9),
             texture = 'textures\\saloon',
             rotation = (90,0,0),
             collider = 'mesh'
            )

#L1 = PointLight(y = -2, z = 2, color = color.black, scale = 10)
#L2 = PointLight(y = -5, z = 10, color = color.blue, scale = 100)
L3 = PointLight(y = 10,x = 2, z = 1, color = color.red, scale = 1)

# [ Functions ]--------------------------------------------------------------------------------------------------------[]


# [ Update Function ]--------------------------------------------------------------------------------------------------[]

def update():
    global movespeed

    if held_keys[runBIND]:
        movespeed = walkspeed + runspeed # A movespeed egyenlo a jatekos es a kamera sebessegevel
    else:
        movespeed = walkspeed # kivonja a futasi sebesseg ereteket.

    camera_control(player, camera_maxheight, camera_maxwidth, move_upBIND, move_downBIND, move_rightBIND, move_leftBIND, movespeed)

# []-------------------------------------------------------------------------------------------------------------------[]










app.run()










