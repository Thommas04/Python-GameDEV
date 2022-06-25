
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

front_anim_counter = 0
def front_anim(refresh, upper_body, lower_body):
    global front_anim_counter, block

    if refresh == True:
        if held_keys['s']:
            front_anim_counter += 1
            upper_body.texture = 'textures\\main_character\\front_view\\upper_body\\front_anim_up' + str(front_anim_counter)
            lower_body.texture = 'textures\\main_character\\front_view\\lower_body\\front_anim' + str(front_anim_counter)
            if front_anim_counter == 8:
                front_anim_counter = 0













