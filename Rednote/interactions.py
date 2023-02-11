
from ursina import *

entrance_layer = -0.7
dest_layer = -0.1

class Interior(Button):
    def on_hover(self):
        print('kurzormegváltozik')
    def on_leave(self):
        print('kurzorvissza')

    def __init__(self, position, destination, id, player):
        super().__init__(parent=scene,
            position = [position[0], position[1], entrance_layer],
            model='quad',
            alpha = 0.5,
            tag='interior_marker',
            on_mouse_enter = Func(Interior.on_hover, self),
            on_mouse_exit = Func(Interior.on_leave, self),
            on_click = Func(Interior.load_interior, self, True))

        self.pos = position
        self.destination = destination
        self.id = id
        self.player = player

        self.intexit  = Entity(alpha = 0.5, model='quad', scale=(1,2,0), position=(destination[0], destination[1], dest_layer), color=color.red, tag = 'interior_marker')

        self.player.interior_marker_list.append([self.intexit, self])

    def load_interior(self, entrance = False):
        if entrance:
            print(distance(self.player.position, self.position))
            if distance(self.player.position, self.position) < 1:
                print(self.destination)
                self.player.interior_exit_enable_byte = False
                for parts in self.player.player_parts:
                    parts.x += self.destination[0] - self.pos[0]
                    parts.y += self.destination[1] - self.pos[1]


        else:
            for parts in self.player.player_parts:
                parts.x += self.pos[0] - self.destination[0]
                parts.y += self.pos[1] - self.destination[1]
            return self.pos





