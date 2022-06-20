
from ursina import *

def camera_control(player, camera_maxheight, camera_maxwidth, move_upBIND, move_downBIND, move_rightBIND, move_leftBIND, movespeed):

    if camera.y <= camera_maxheight:
        camera.y += held_keys[ move_upBIND ] * movespeed * time.dt
        player.y += held_keys[ move_upBIND ] * movespeed * time.dt

    if camera.y >= -camera_maxheight:
        camera.y -= held_keys[ move_downBIND ] * movespeed * time.dt
        player.y -= held_keys[ move_downBIND ] * movespeed * time.dt

    if camera.x >= -camera_maxwidth:
        camera.x -= held_keys[ move_leftBIND ] * movespeed * time.dt
        player.x -= held_keys[ move_leftBIND ] * movespeed * time.dt

    if camera.x <= camera_maxwidth:
        camera.x += held_keys[ move_rightBIND ] * movespeed * time.dt
        player.x += held_keys[ move_rightBIND ] * movespeed * time.dt