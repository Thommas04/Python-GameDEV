from ursina import *

app = Ursina()

global_time = 0 #
last_time = 0

def update():
    global global_time, last_time
    global_time += time.dt
    if global_time - last_time > 2: # 2 másodpercenként
        print(last_time)
        last_time = global_time


app.run()