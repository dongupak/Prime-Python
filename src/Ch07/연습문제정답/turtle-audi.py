import turtle
 
t = turtle.Turtle()
t.pensize(4)
t.hideturtle()
for i in range(4):
  t.penup()
  t.goto(i*70-100, -50)
  t.pendown()
  t.circle(50)
