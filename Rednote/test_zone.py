
# URSINA IMPORTS
from ursina import *
from ursina.shaders import lit_with_shadows_shader

# Own modules
from collisions import *
from time import sleep
from functions import *
from threading import *
from player import *
from objects import *
from anims import *

app = Ursina()

weapon_wheel = 'hud/weapon_wheel/weapon_wheel.png'
minimap = 'hud/hud_widgets/minimap/minimap_frame.png'

EditorCamera()
create_net() # keszit egy halot

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

scene.fog_density = (100, 150)   # sets linear density start and end

#L1 = PointLight(shadows = True, y = -2, z = 100, color = color.rgb(255,255,255), scale = 1000)

#PointLight(shadows = True, scale = 1, x = 0, y = 0, z = 10, color = color.rgba(0, 255, 255, 1000))
minimap = Entity(texture = minimap, model = 'quad', position = (0,0,0), scale = (0.4, 0.4, 0), alpha = 1)


'''xx = 10
def light():
    global L1, xx
    xx += 1
    print(xx)
    L1.color = color.rgb(xx,xx,xx)

    invoke(light, delay = 0.1)'''

#light()

L2 = AmbientLight(y = -5, z = -100, color = color.blue, scale = 1000)
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
world_canvas = Entity(color = color.green, model = 'cube', collider = 'box', scale = (192,108,0), position = (0,0,.1), tag = 'canvas')
townlevel_collision()

# []-------------------------------------------------------------------------------------------------------------------[]

app.run()
