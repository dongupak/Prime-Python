import turtle
import random

def sun_drawing(tu, c1, c2, deg):
    #tu.color(c1, c2)
    tu.color('red', 'yellow')
    tu.begin_fill()
    pos = tu.pos()
    while True:
        tu.forward(300)
        tu.left(deg)
        if abs(tu.pos() - pos) < 1: # 
            break
    tu.end_fill()

t = turtle.Turtle()
t.hideturtle()
t.speed('fastest') #
t.penup()

t.goto(random.randint(-100, 100), random.randint(-100, 0))
t.pendown()
sun_drawing(t, 'red', 'yellow', random.randint(-0, 170))
t.penup()
t.goto(random.randint(-100, 100), random.randint(-100, 0))
t.pendown()
sun_drawing(t, 'red', 'yellow', random.randint(-0, 100))
t.penup()
t.goto(random.randint(-100, 100), random.randint(-100, 0))
t.pendown()
sun_drawing(t, 'red', 'yellow', random.randint(-0, 200))
t.penup()
t.goto(random.randint(-100, 100), random.randint(-100, 0))
t.pendown()
sun_drawing(t, 'red', 'yellow', random.randint(-0, 200))
turtle.done()
