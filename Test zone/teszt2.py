from ursina import *
from ursina.raycaster import raycast

app = Ursina()
EditorCamera()

faceing = Vec3(1,0,0)

class Player(Entity):
    def update(self):
        global faceing
        self.direction = Vec3(self.up * (held_keys['w'] - held_keys['s'])+ self.right * (held_keys['d'] - held_keys['a'])).normalized()  # get the direction we're trying to walk in.

        origin = self.world_position + (self.up*.5)

        if held_keys['d']:
            faceing = Vec3(1,0,0)
        elif held_keys['w']:
            faceing = Vec3(0,1,0)
        elif held_keys['a']:
            faceing = Vec3(-1,0,0)
        elif held_keys['s']:
            faceing = Vec3(0,-1,0)

        hit_info = boxcast(origin , faceing, ignore=(self,), distance=.5, debug=True, thickness = (1,1))
        if not hit_info.hit:
            self.position += self.direction * 5 * time.dt
        else:
            print('got hit')

Player(model='cube', origin_y=-.5, color=color.orange, collider = 'box', scale=(1,1,1))

Entity(model='cube', collider='mesh', scale=(3,5,0), color = color.azure)
Entity(model='cube', collider='mesh', scale=(3,5,0), color=color.azure, x=8)

app.run()