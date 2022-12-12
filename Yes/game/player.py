from ursina import *

class Player(Entity):
    def __init__(self, tex_ture, **kwargs):
        super().__init__()

        self.model = 'cube'
        self.origin_y = -.5
        self.scale_y = 2
        self.color = color.orange
        self.collider = 'box'

        self.walk_speed = 8
        self.walking = False
        self.velocity = 0 # a mozgás iránya 1 jobbra -1 balra
        self.jump_height = 4
        self.jump_duration = .5
        self.jumping = False
        self.max_jumps = 2
        self.jumps_left = self.max_jumps
        self.gravity = 1
        self.grounded = True
        self.air_time = 0  # növeli a sebességet zuhanáskor
        self.traverse_target = scene # a scene-hez van rögzítve
        self._start_fall_sequence = None
        self.control = None
        self.tex_ture = tex_ture

        print(self.tex_ture)
        self.character_texture = Entity(texture = self.tex_ture, rotation = (-90,0,0),model='plane', scale=(1, 0, 1), position=(0, 0.5, -1.5), parent = self, double_sided = True)

        ray = boxcast(self.world_position, self.down, distance=10, ignore=(self, ), traverse_target=self.traverse_target, thickness=.9)
        if ray.hit:
            self.y = ray.world_point[1] + .01
        # camera.add_script(SmoothFollow(target=self, offset=[0,1,-30], speed=4))

        for key, value in kwargs.items():
            setattr(self, key, value)

        # delay_gravity one frame
        target_gravity = self.gravity
        self.gravity = 0
        invoke(setattr, self, 'gravity', target_gravity, delay=1/60)
        self._original_scale_x = self.scale_x


    def update(self):
        if boxcast(
            self.position+Vec3(self.velocity * time.dt * self.walk_speed,self.scale_y/2,0),
            # self.position+Vec3(sefl,self.scale_y/2,0),
            direction=Vec3(self.velocity,0,0),
            distance=abs(self.scale_x/2),
            ignore=(self, ),
            traverse_target=self.traverse_target,
            thickness=(self.scale_x*.9, self.scale_y*.9),
            ).hit == False:

            self.x += self.velocity * time.dt * self.walk_speed

        self.walking = held_keys[self.control[1]] + held_keys[self.control[3]] > 0 and self.grounded

        # ellenőrzi hogy a földön vagy e
        ray = boxcast(
            self.world_position+Vec3(0,.1,0),
            self.down,
            distance=max(.15, self.air_time * self.gravity),
            ignore=(self, ),
            traverse_target=self.traverse_target,
            thickness=self.scale_x*.9,
            #debug=True
            )

        # print(self.grounded)
        if ray.hit:
            if not self.grounded:
                self.land()
            self.grounded = True
            self.y = ray.world_point[1]
            return
        else:
            self.grounded = False

        # if not on ground and not on way up in jump, fall
        if not self.grounded and not self.jumping:
            self.y -= min(self.air_time * self.gravity, ray.distance-.1)
            self.air_time += time.dt*4 * self.gravity

        # ütközéskor zuhanjon
        if self.jumping:
            if boxcast(self.position+(0,.1,0), self.up, distance=self.scale_y, thickness=.95, ignore=(self,), traverse_target=self.traverse_target).hit:
                self.y_animator.kill()
                self.air_time = 0
                self.start_fall()

    def input(self, key):
        if key == self.control[0]: # space ['space', 'd', 'd up', 'a', 'a up']
            self.jump()

        if key == self.control[1]: # d
            self.velocity = 1
            self.scale_x = self._original_scale_x
        if key == self.control[2]: # d up
            self.velocity = -held_keys[self.control[3]]

        if key == self.control[3]: # a
            self.velocity = -1
        if key == self.control[4]: # a up
            self.velocity = held_keys[self.control[1]]

        if held_keys[self.control[1]] or held_keys[self.control[3]]: # a - d
            self.character_texture.scale_x = self._original_scale_x * self.velocity


    def jump(self):
        if not self.grounded and self.jumps_left <= 1:
            return

        if self._start_fall_sequence:
            self._start_fall_sequence.kill()

        # don't jump if there's a ceiling right above us
        if boxcast(self.position+(0,.1,0), self.up, distance=self.scale_y, thickness=.95, ignore=(self,), traverse_target=self.traverse_target).hit:
            return

        if hasattr(self, 'y_animator'):
            self.y_animator.kill()
        self.jump_dust = Entity(model=Circle(), scale=.5, color=color.white33, position=self.position)
        self.jump_dust.animate_scale(3, duration=.3, curve=curve.linear)
        self.jump_dust.fade_out(duration=.2)
        destroy(self.jump_dust, 2.1)

        self.jumping = True
        self.jumps_left -= 1
        self.grounded = False

        target_y = self.y + self.jump_height
        duration = self.jump_duration
        # check if we hit a ceiling and adjust the jump height accordingly
        hit_above = boxcast(self.position+(0,self.scale_y/2,0), self.up, distance=self.jump_height-(self.scale_y/2), thickness=.9, ignore=(self,))
        if hit_above.hit:
            target_y = min(hit_above.world_point.y-self.scale_y, target_y)
            try:
                duration *= target_y / (self.y+self.jump_height)
            except ZeroDivisionError as e:
                return e

        self.animate_y(target_y, duration, resolution=30, curve=curve.out_expo)
        self._start_fall_sequence = invoke(self.start_fall, delay=duration)

    def start_fall(self):
        self.y_animator.pause()
        self.jumping = False

    def land(self):
        # print('land')
        self.air_time = 0
        self.jumps_left = self.max_jumps
        self.grounded = True
