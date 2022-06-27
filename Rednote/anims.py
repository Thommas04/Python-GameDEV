
from ursina import *

block = False

def set_block():
    global block
    if block == False:
        block = True
def reset_block():
    global block
    if block == True:
        block = False
        invoke(set_block, delay=reset_delay)

# ---------------------------------------------------------------------------------------------------------------------[]

front_delay = -1
front_duration = 2
reset_delay = 0.35

# ezeket egyelore nem futtatja le semmi
def front_anims_forward(front_right_arm, front_left_arm, front_right_leg, front_left_leg):
    global block
    if block == False:
        pass
        invoke(set_block, delay = reset_delay)

def front_anims_backward(front_right_arm, front_left_arm, front_right_leg, front_left_leg):
    global block
    if block == True:
        front_right_arm.animate('rotation_x',55, duration = front_duration, delay = front_delay, curve = curve.linear, interrupt='kill')
        invoke(reset_block, delay = reset_delay)

# ---------------------------------------------------------------------------------------------------------------------[]

player_facing = "front" # cser�jed le animatorra

front_anim_counter = 0
back_anim_counter = 0
right_anim_counter = 0
left_anim_counter = 0
def front_anim(refresh, upper_body, lower_body):
    global front_anim_counter, back_anim_counter, right_anim_counter, left_anim_counter, block, player_facing

    if refresh == True:
        if held_keys['s']:
            front_anim_counter += 1
            player_facing = "front"
            upper_body.texture = 'textures\\main_character\\front_view\\upper_body\\front_anim_up' + str(front_anim_counter)
            lower_body.texture = 'textures\\main_character\\front_view\\lower_body\\front_anim' + str(front_anim_counter)
            if front_anim_counter == 8:
                front_anim_counter = 0
        if held_keys['s'] == False and player_facing == "front":
            upper_body.texture = 'textures\\main_character\\front_view\\upper_body\\front_anim_up' + str(front_anim_counter + 1)
            lower_body.texture = 'textures\\main_character\\front_view\\lower_body\\front_anim' + str(front_anim_counter + 1)
            if front_anim_counter >= 1:
                front_anim_counter -= 1

        if held_keys['w']:
            back_anim_counter += 1
            player_facing = "back"
            upper_body.texture = 'textures\\main_character\\back_view\\upper_body\\back_anim' + str(back_anim_counter)
            lower_body.texture = 'textures\\main_character\\back_view\\lower_body\\back_anim_up' + str(back_anim_counter)
            if back_anim_counter == 8:
                back_anim_counter = 0
        if held_keys['w'] == False and player_facing == "back":
            upper_body.texture = 'textures\\main_character\\back_view\\upper_body\\back_anim' + str(back_anim_counter + 1)
            lower_body.texture = 'textures\\main_character\\back_view\\lower_body\\back_anim_up' + str(back_anim_counter + 1)
            if back_anim_counter >= 1:
                back_anim_counter -= 1

        if held_keys['d']:
            right_anim_counter += 1
            player_facing = "right"
            upper_body.texture = 'textures\\main_character\\right_view\\upper_body\\right_anim_up' + str(right_anim_counter)
            lower_body.texture = 'textures\\main_character\\right_view\\lower_body\\right_anim' + str(right_anim_counter)
            if right_anim_counter == 8:
                right_anim_counter = 0
        if held_keys['d'] == False and player_facing == "right":
            upper_body.texture = 'textures\\main_character\\right_view\\upper_body\\right_anim_up' + str(right_anim_counter + 1)
            lower_body.texture = 'textures\\main_character\\right_view\\lower_body\\right_anim' + str(right_anim_counter + 1)
            if right_anim_counter >= 1:
                right_anim_counter -= 1

        if held_keys['a']:
            left_anim_counter += 1
            player_facing = "left"
            upper_body.texture = 'textures\\main_character\\left_view\\upper_body\\left_anim_up' + str(left_anim_counter)
            lower_body.texture = 'textures\\main_character\\left_view\\lower_body\\left_anim' + str(left_anim_counter)
            if left_anim_counter == 8:
                left_anim_counter = 0
        if held_keys['a'] == False  and player_facing == "left":
            upper_body.texture = 'textures\\main_character\\left_view\\upper_body\\left_anim_up' + str(left_anim_counter + 1)
            lower_body.texture = 'textures\\main_character\\left_view\\lower_body\\left_anim' + str(left_anim_counter + 1)
            if left_anim_counter >= 1:
                left_anim_counter -= 1
        camera.shake(duration=.2, magnitude=0.01, speed=1, direction=(100, 100))










