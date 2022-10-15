from ursina import *

app = Ursina()

a = 0

stage = 1
def slow_check():
    global stage
    if stage == 2:
        stage = 100
    if stage == 1:
        stage = 2

    invoke(slow_check, delay = 3)
slow_check()

def update():
    global a
    if stage == 2:
        a += 1

def input(key):
    if key == 'left mouse down':
        print(a)



app.run()