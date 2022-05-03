

import turtle
turtle.bgcolor("black")
turtle.pensize(5)
turtle.speed(1)
b=["red","blue","green","purple","yellow"]
for i in range(4):
    for a in b:
        turtle.color(a)
        turtle.square(50)
        turtle.left(5)
turtle.mainloop()


import turtle
turtle.bgcolor("black")
turtle.pensize(5)
turtle.speed(1)
b=["red","blue","green","purple","yellow"]
for i in range(4):
    for a in b:
        turtle.color(a)
        turtle.circle(50)
        turtle.left(5)
turtle.mainloop()