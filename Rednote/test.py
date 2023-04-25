from ursina import *

app = Ursina()

num_sides = 50

verts = []
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    x = 0.5 * math.cos(angle)
    y = 0.5 * math.sin(angle)
    verts.append((x, y, 0))

tris = []
for i in range(1, num_sides - 1):
    tris.append((0, i, i+1))

uvs = []
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    u = (math.cos(angle) + 1) / 2
    v = (math.sin(angle) + 1) / 2
    uvs.append((u, v))

polygon = Entity(texture_scale = (0.2,0.2,0),texture='hud/hud_widgets/minimap/minimap_bg.jpg', model=Mesh(vertices=verts, triangles=tris, uvs=uvs), position = (-0.685, -0.326, -0.04),scale = (0.24, 0.24), parent = camera.ui)

x = 73
y = 130
polygon.texture_offset = (((x / 2) / 100) - 0.1, ((y / 2) / 100) - 0.1)

EditorCamera()

app.run()
