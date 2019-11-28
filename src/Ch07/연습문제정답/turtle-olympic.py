import turtle
 
t = turtle.Turtle()
t.hideturtle()
#t.goto(-100, 0)
t.pensize(6) #Set the thickness of the pen to 6
firstRowColors = ["blue", "black", "red"] #firstRowColors is a list of colors that are present in the first row of logo
for i in range(3):
  t.penup()
  t.pencolor(firstRowColors[i])
  t.goto(i*110-100, -25)
  t.pendown()
  t.circle(50)
 
secondRowColors = ["", "yellow", "", "green"]
for i in range(1, 4, 2):
  t.penup()
  t.pencolor(secondRowColors[i])
  t.goto(i*55-100, -75)
  t.pendown()
  t.circle(50)
