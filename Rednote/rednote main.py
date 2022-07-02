
# URSINA IMPORTS
from ursina import *
from ursina.shaders import lit_with_shadows_shader

# Own modules
from collisions import *
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


# ---------------------------------------------------------------------------------------------------------------------[]
# [ Variables ]--------------------------------------------------------------------------------------------------------[]

# camera :
camera.fov = 60 # default [ field of view ]

# [ END Variables ]----------------------------------------------------------------------------------------------------[]
# ---------------------------------------------------------------------------------------------------------------------[]
# [Declare Objects]----------------------------------------------------------------------------------------------------[]

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

townlevel_collision()

# []-------------------------------------------------------------------------------------------------------------------[]

app.run()
