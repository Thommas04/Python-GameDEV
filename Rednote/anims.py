
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

# ---------------------------------------------------------------------------------------------------------------------[]

front_delay = -1
front_duration = 2
reset_delay = 0.35

def front_anims_forward(front_right_arm, front_left_arm, front_right_leg, front_left_leg):
    global block
    if block == False:
        front_right_arm.animate('rotation_x',100, duration = front_duration, delay = front_delay, curve = curve.linear, interrupt='kill')
        front_left_arm.animate('rotation_x',40,  duration = front_duration, delay = front_delay, curve = curve.linear, interrupt='kill')
        front_right_leg.animate('rotation_x',50, duration = front_duration, delay = front_delay, curve = curve.linear, interrupt='kill')
        front_left_leg.animate('rotation_x',110, duration = front_duration, delay = front_delay, curve = curve.linear, interrupt='kill')
        invoke(set_block, delay = reset_delay)

def front_anims_backward(front_right_arm, front_left_arm, front_right_leg, front_left_leg):
    global block
    if block == True:
        front_right_arm.animate('rotation_x',55, duration = front_duration, delay = front_delay, curve = curve.linear, interrupt='kill')
        front_left_arm.animate('rotation_x',90,  duration = front_duration, delay = front_delay, curve = curve.linear, interrupt='kill')
        front_right_leg.animate('rotation_x',110,duration = front_duration, delay = front_delay, curve = curve.linear, interrupt='kill')
        front_left_leg.animate('rotation_x',50,  duration = front_duration, delay = front_delay, curve = curve.linear, interrupt='kill')

        invoke(reset_block, delay = reset_delay)

# ---------------------------------------------------------------------------------------------------------------------[]