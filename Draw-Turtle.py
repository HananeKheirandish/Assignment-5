from datetime import time
import turtle
import time

t = turtle.Pen()
t.shape('turtle')
pos1 = 0
pos2 = 0
for i in range(10):
    t.penup()
    t.setpos(pos1 , pos2)
    t.pendown()
    for j in range(i+3):
        t.forward(130)
        t.left(360 / (i+3))
    pos1 -= 1
    pos2 -= 20
    t.penup()
    t.setpos(pos1 , pos2)
    t.pendown()
time.sleep(1)