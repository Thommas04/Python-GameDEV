
from ursina import *

faceing = Vec3(1,0,0) # megadja a boxcast iranyat
thickness = (1,1) # megadja a boxcast nagysagat.

# ---------------------------------------------------------------------------------------------------------------------[]
# [ KeyBINDS ]---------------------------------------------------------------------------------------------------------[]

runBIND = "shift"

move_upBIND = "w"
move_downBIND = "s"
move_leftBIND = "a"
move_rightBIND = "d"

# ---------------------------------------------------------------------------------------------------------------------[]
# [ Variables ]--------------------------------------------------------------------------------------------------------[]

walkspeed = 5 # A karakter es a kamera mozgasi sebessege, WASD-vel.
runspeed = 10 # Ezt a mennyiseget adja hozza a jatekos walkspeedjehez.

player_scale = (1.2, 0, -1.67)

# [ Player Class ] ----------------------------------------------------------------------------------------------------[]

class Player(Entity):
    def update(self):
        global faceing, thickness
        origin = self.world_position + (0,-0.9,0.5)

        if held_keys['d']:
            faceing = Vec3(0.01,0,0)
        elif held_keys['w']:
            faceing = Vec3(0,0.01,0)
        elif held_keys['a']:
            faceing = Vec3(-0.01,0,0)
        elif held_keys['s']:
            faceing = Vec3(0,-0.01,0)

        # A boxcast egy hitbox mely erzekeli, ha colliderrel rendelkezo entitasnak utkozott.
        hit_info = boxcast(origin, faceing, ignore=(self, upper_body), distance=0.8, debug=False, thickness = (1,1))

        if held_keys[runBIND]:
            movespeed = walkspeed + runspeed  # A movespeed egyenlo a jatekos es a kamera sebessegevel
        else:
            movespeed = walkspeed

        if not hit_info.hit:
            for i in range(0, len(list)):
                list[i].y += held_keys[move_upBIND] * movespeed * time.dt
            for i in range(0, len(list)):
                list[i].y -= held_keys[move_downBIND] * movespeed * time.dt
            for i in range(0, len(list)):
                list[i].x += held_keys[move_rightBIND] * movespeed * time.dt
            for i in range(0, len(list)):
                list[i].x -= held_keys[move_leftBIND] * movespeed * time.dt
        else:
            pass #print(hit_info.distance)

# [] ------------------------------------------------------------------------------------------------------------------[]

upper_body = Entity(model = 'plane',
                    position = Vec3(0, 0, -0.5),
                    scale = player_scale,
                    rotation = (90, 0, 0),
                    collider = 'mesh',
                    texture = 'textures\\main_character\\front_view\\upper_body\\front_anim_up1'
                    )

lower_body = Player(model = 'plane',
                    collider = 'box',
                    scale = player_scale,
                    position = Vec3(0, 0.005, -0.4),
                    rotation = (90,0,0),
                    texture = 'textures\\main_character\\front_view\\lower_body\\front_anim1'
                    )

follow = SmoothFollow(target = upper_body, speed = 10, offset = [0,0,-15])
#camera.add_script(follow)

list = [upper_body, lower_body]

# [] ------------------------------------------------------------------------------------------------------------------[]