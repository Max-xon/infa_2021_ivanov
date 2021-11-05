import random
import turtle
from random import  *

nubmer_of_turtle = 5

border=turtle.Turtle()
border.shape('circle')
border.speed(0)
border.color("pink")
border.width(5)
border.hideturtle()
border.penup()
border.goto(250,0)
border.down()
border.goto(250,250)
border.goto(-250,250)
border.goto(-250,-250)
border.goto(250,-250)
border.goto(250,0)
pool = [turtle.Turtle(shape='circle') for i in range(nubmer_of_turtle)]

for unit in pool:
    unit.penup()
    unit.speed(10)
    unit.goto(randint(-245, 245), randint(-245, 245))

vx = 10
vy = 10
speedx = [vx for i in range(nubmer_of_turtle)]
speedy = [vy for i in range(nubmer_of_turtle)]
for i in range(100000):
    for unit in range(len(pool)):
        x, y = pool[unit].position()
        x += speedx[unit]
        y += speedy[unit]
        pool[unit].goto(x, y)
        for unit2 in range(len(pool)):
            if pool[unit] != pool[unit2]:
                x2, y2 = pool[unit2].position()
                dx = abs(x - x2)
                dy = abs(y - y2)
                if dx <= 13 and dy <= 13:
                    speedy[unit] = -speedy[unit]
                    speedy[unit2] = -speedy[unit2]
                    speedx[unit] = -speedx[unit]
                    speedx[unit2] = -speedx[unit2]
        if x > 247 or x < - 247:
            speedx[unit] = -speedx[unit]
        if y > 247 or y < - 247:
            speedy[unit] = -speedy[unit]

turtle.mainloop()