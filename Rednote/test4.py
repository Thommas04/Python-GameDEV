import math
from ursina import *

# Set up the window
app = Ursina()

# Set the field dimensions
field_width = 40
field_height = 10

# Create the ball entity
ball = Entity(model='sphere', color=color.orange, position=(0,0,0), scale=0.5)

# Set the ball's initial velocity
velocity = Vec3(2, 2, 0)

# Set the ball's bounciness (coefficient of restitution)
bounciness = 0.8

# Set the ball's gravity
gravity = Vec3(0, -0.02, 0)

# Create the player 1 and player 2 entities
player1 = Entity(model='cube', collider = 'box', color=color.red, position=(-field_width/2 + 1, 0, 0), scale=Vec3(0.5, 2, 0.5))
player2 = Entity(model='cube', collider = 'box', color=color.blue, position=(field_width/2 - 1, 0, 0), scale=Vec3(0.5, 2, 0.5))

# Set the player movement speed
movement_speed = 3

bx_direction = 0.4
by_direction = 0.04
def check_collide(E1, E2):
    global bx_direction,by_direction
    if E1.x < E2.x + E2.scale_x and E1.x + E1.scale_x > E2.x:
        if E2.y < E1.y + E1.scale_y and E2.y + E2.scale_y > E1.y:
            bx_direction = bx_direction*-1
            by_direction = by_direction*-1

            #if E1 == player1:
            #    print('ütközés')


def update():
    global velocity
    # Update the ball's position based on its velocity
    ball.position += velocity * time.dt * 10

    # Check if the ball has hit a wall and reverse its velocity if it has
    if ball.x > field_width/2:
        velocity.x = -abs(velocity.x) * bounciness
    elif ball.x < -field_width/2:
        velocity.x = abs(velocity.x) * bounciness

    if ball.y > field_height/2:
        velocity.y = -abs(velocity.y) * bounciness
    elif ball.y < -field_height/2:
        velocity.y = abs(velocity.y) * bounciness

    # Apply gravity to the ball's velocity
    velocity += gravity * 4

    check_collide(player1, ball)
    check_collide(player2, ball)

    # Check if the player 1 or player 2 keys are pressed and move the corresponding player
    if held_keys['a']:
        player1.x -= movement_speed * time.dt
    if held_keys['d']:
        player1.x += movement_speed * time.dt
    if held_keys['w']:
        player1.y += movement_speed * time.dt
    if held_keys['s']:
        player1.y -= movement_speed * time.dt
    if held_keys['left arrow']:
        player2.x -= movement_speed * time.dt
    if held_keys['right arrow']:
        player2.x += movement_speed * time.dt
    if held_keys['up arrow']:
        player2.y += movement_speed * time.dt
    if held_keys['down arrow']:
        player2.y -= movement_speed * time.dt

# Start the game loop

EditorCamera()
app.run()