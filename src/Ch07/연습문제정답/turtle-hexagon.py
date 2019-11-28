import turtle
 
t = turtle.Turtle()
t.penup()
t.goto(-50, 50)
t.pendown()
for i in range(6):
   t.forward(100) #Assuming the side of a pentagon is 100 units
   t.right(60) #Turning the turtle by 72 degree
