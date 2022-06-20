



# Python-GameDEV

Tisztelt nberek, �llatok, cs�sz�m�sz�k �s egy�b �gi szerzetesek, drogd�lerek, maszkulinok, orosz c�rok, Orb�n Viktorok �s tisztelt egybegy�lt famili�risan pigment�lt egy�n� egy�nis�gek.

Ursina - GLHF
Grayhollow / Rustfort

--------------------------------------------------------------
--------------------------------------------------------------

Alapok:

# Application

	from ursina import *

- Ha FPS n�zet� programr�l van sz�:

	from ursina.prefabs import first_person_controller

from ursina.prefabs.first_person_controller import FirstPersonController

-------------------------

	app = Ursina()

- Ha FPS n�zet� programr�l van sz�:

		player = FirstPersonController()


	{ Program }

	app.run()

-------------------------

# Text 

	szoveg = Text(text = 'Sz�veg', scale = 1, x = 0.1, y = 0.1, color = color.red)



--------------------------------------------------------------
--------------------------------------------------------------

# Entity 

Az Ursin�ban az entit�sok azok az objektumok, amik a vil�gban teret foglalnak ak�r 2D-ben, ak�r 3D-ben. 

# Entity - Model

- e = Entity(model = 'file')

A file kiterjeszt�se: .obj

El�re ledefini�lt modellek: 

	- Quad
	- Plane
	- Cube
	- Sphere

--------------------------------------------------------------
--------------------------------------------------------------
--------------------------------------------------------------

# Entity - texture

	e = Entity(model = 'Plane', texture = 'texturefile')

A texturefile kiterjeszt�se: .png , de lehet .mp4 is! 

PIL modullal:

	texture = PIL.Image.new(mode = "RGBA", size = (854,480))

--------------------------------------------------------------


# Entity - Scale

	e = Entity(model = 'Cube', Scale = (3, 1, 1))

--------------------------------------------------------------

# Entity - Color

	e.color = color.red
	e.color = color.rgb(0.8, 0.1, 0)
	e.color = color.random_color()

--------------------------------------------------------------

# Entity - Position

Az entit�sok viszony�that�k a vil�g k�z�ppontj�hoz (0, 0, 0)
De ak�r egym�shoz k�pest is.

	parent_entity = Entity(position = Vec3(0, 2, 0))

	e = Entity(parent = parent_entity,position = Vec3(0,2,0))

	print(e.position) --> Vec3(0,2,0)
	print(e.world_position) --> Vec3(0, -2, 0)

ugyanis: (0, 2, 0) position - (0, 4, 0) world_position

[][][][][][][][]

	e.world_position = Vec3(0, 0, 0)
	print(e.position) --> Vec3(0, -2, 0)

Teh�t az al�rendelt objektumok k�vetik a sz�l� objektumot. 

--------------------------------------------------------------

# Entity - Rotation

	e.rotation = (0, 0, 0)
	e. rotation_y = 90

Van egy be�p�tett f�ggv�ny, ami �gy forgatja az objektumot, hogy az egy m�sik objektumra n�zzen.

	look_at()

pl: 

	other_entity = Entity(position = (0, 1, 0))
	e.look_at(other_entity, axis = 'up')


--------------------------------------------------------------

# Entity - Update

	e = Entity()
	
	def my_update():
		e.x += 1 * time.dt # delta time (since last frame)

	e.update = my_update

vagy

	class Player(Entity):
		def update(self):
			self.x += 1 * time_dt


--------------------------------------------------------------

# Entity - Input

	class Player(Entity):
		def input(self, key):
			if key == 'w':
				self.position += self.forward
			
			if key == 'd':
				self.animate('rotation_y', self.rotation_y + 90, duration = 0.1)
			
			if key == 'a':
				self.animate('rotation_y', self.rotation_y - 90, duration = 0.1)


--------------------------------------------------------------

# Entity - Mouse Input

- Ha az entit�s a kurzor alatt van:
	
	print(mouse.hovered_entity)

- Ellen�rzi, ha az entity aminek van colliderje azt a kurzor hovereli.

	print(my_entity.hovered)

T�bb lehet�s�g:

	- on_click()
	- on_double_click()
	- on_mouse_enter()
	- on_mouse_exit()

[][][][][][]

Pl:

	def action():
		print('clicked')

	
	Entity(model = 'quad', parent = camera.ui, scale = 0.1, collider = 'box', on_click = action)

[][][][][][]

- Side effectek ki / be kapcsolhat�k (pl anim�ci�kn�l)

	- on_enable()
	- on_disable()

--------------------------------------------------------------

# Entity - Coordinate System

 	 y ( up )

	z  |
	\ |
	 \|_____________ x ( right )


# UI Coordinate System

	_______________________(.5, .5)____(window.top_right)
	|       '                  '       |
	|       '                  '       |
	|       '                  '       |
	|       '                  '       |
	|       '      (0, 0)      '       |(.5*window.aspect_ratio,0)
	|       '                  '       |
	|       '                  '       |
	|       '                  '       |
	|_______'__________________'_______|
	    (-.5, -.5)


# Rotation

           _______
          /
          \->
  	  __
  	 /  \     y
  	|   v     |
  	|      z  |                __
  	        \ |               /  \
  	         \|               v   |
 	           ---------- x       |
                              |



# Origin


	            (-.5,.5)
	+--------+      *--------+
	|        |      |        |
	|  (0,0) |      |        |
	|        |      |        |
	+--------+      +--------+
	
	  (0,.5)
	+----*---+      +--------+
	|        |      |        |
	|        |      |        * (.5,0)
	|        |      |        |
	+--------+      +--------+



--------------------------------------------------------------

--------------------------------------------------------------

--------------------------------------------------------------

# EXAMPLES



from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

ground = Entity(model='plane', texture='textures\\ground', scale=10, collider='box')
player = FirstPersonController(model='cube', origin_y=-.5, color=color.orange, has_pickup=False)
camera.z = -1

pickup = Entity(model='sphere', position=(1,.5,3))

def update():
    if not player.has_pickup and distance(player, pickup) < pickup.scale_x * 2:
        print('pickup')

        print(distance(player, pickup))
        print('ok')

        player.has_pickup = True
        pickup.animate_scale(0, duration=.1)
        destroy(pickup, delay=1)

app.run()




























