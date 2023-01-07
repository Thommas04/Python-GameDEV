from ursina import *

class Inventory(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            texture = None,
            texture_scale = (4,4),
            scale = (.43, .43),
            origin = (-.5, .5),
            position = (-0.24,0.275),
            color = color.color(0,0,.1,.9))

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.background = Entity(texture = inventory_background, alpha = 1, scale = (0.62, 1.024, -0.12), position=[0, 0, 0], model='quad', parent=camera.ui)

    # [] ------------------------------------------------------------------------------------------------------------- []

    def find_free_spot(self, tagged): # Keres egy üres helyet, és visszadja az x, y koordinátáját.
        for y in range(4):
            for x in range(4):
                new_children_list = []
                for i in self.children:
                    if i.tag == tagged:
                        new_children_list.append(i)

                grid_positions = [(int(e.x*self.texture_scale[0]), int(e.y*self.texture_scale[1])) for e in new_children_list]
                print(grid_positions)

                if not (x,-y) in grid_positions:
                    return x, y

    # [] ------------------------------------------------------------------------------------------------------------- []

    def append(self, item, tagged, x = 0, y = 0): # Hozzáad egy itemet
        if len(self.children) >= 4*4: # Lefut, ha tele az inventory
            print('inventory full')
            return

        x, y = self.find_free_spot(tagged) # De előtte keresni kell egy szabad helyet.

        icon = Draggable( parent = self, model = 'quad', texture = item, color = color.white,
            scale_x = 1 / self.texture_scale[0], scale_y = 1 / self.texture_scale[1], origin = (-.5,.5),
            x = x * 1 / self.texture_scale[0], y = -y * 1 / self.texture_scale[1], z = -.5, tag = tagged)

        name = item.replace('_', ' ').title()

        # [] --------------------------------------------------------------------------------------------------------- []

        def drag():
            icon.org_pos = (icon.x, icon.y)
            icon.z -= .01   # azért, hogy a megragadott item a többi réteg felett legyen

        def drop():
            icon.x = int((icon.x + (icon.scale_x/2)) * 4) / 4
            icon.y = int((icon.y - (icon.scale_y/2)) * 4) / 4
            icon.z += .01

            # Ha rossz helyre húzta kerüljön vissza az eredeti helyére.
            if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                icon.position = (icon.org_pos)
                return

            # Ha a pozíció foglalt, cseréljenek helyet
            for c in self.children:
                if c == icon:
                    continue

                if c.tag == icon.tag:
                    if c.x == icon.x and c.y == icon.y:
                        c.position = icon.org_pos

        icon.drag = drag
        icon.drop = drop




if __name__ == '__main__':
    app = Ursina()


    inventory_background = 'hud/inventory/widgets/inventory_bg.png'
    inventory_buttons_spritesheet = 'hud/inventory/widgets/inventory_buttons_sheet.png'
    inventory_selected_tile = 'hud/inventory/widgets/inventory_selected_tile.png'

    inventory = Inventory()



    def add_item(stat):
        inventory.append(random.choice(('bag', 'bow_arrow', 'gem', 'orb', 'sword')), tagged = stat)

    add_item('tonic')
    add_item('tonic')
    add_item('food')
    add_item('food')
    add_item('food')

    for i in inventory.children:
        i.alpha = 0.1
        if i.tag == 'tonic':
            destroy(i)

    def input(key):
        if key == 'k':
            for i in inventory.children:
                if i.tag == 'food':
                    i.enable()
                if i.tag == 'tonic':
                    i.disable()
        if key == 'j':
            for i in inventory.children:
                if i.tag == 'food':
                    i.disable()
                if i.tag == 'tonic':
                    i.enable()

    app.run()