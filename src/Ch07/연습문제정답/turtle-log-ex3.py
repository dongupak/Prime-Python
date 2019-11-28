import math
import turtle

wn = turtle.Screen()

fred = turtle.Turtle()
sc = turtle.Screen()
sc.reset()

sc.setworldcoordinates(0,-1.5,720,1.5)
fred.width(4)
fred.penup()
fred.goto(0, math.sin(math.radians(0)))
fred.pendown()
fred.color('red')
for angle in range(720):
    y = math.sin(math.radians(angle))
    fred.goto(angle,y)   

fred.penup()
fred.goto(0, math.cos(math.radians(0)))
fred.pendown()
fred.color('green')
for angle in range(720):
    y = math.cos(math.radians(angle))
    fred.goto(angle,y)   

wn.exitonclick()
