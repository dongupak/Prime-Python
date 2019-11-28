import turtle 
import random 

turtles = [] 
colors = ["black", "green", "blue", "red", "grey", "pink"]
n = len(colors)

for index in range(n):
   new_turtle = turtle.Turtle() 
   new_turtle.shape('turtle')
   new_turtle.penup()
   new_turtle.goto(-20, 20)
   turtles.append(new_turtle) 
   
for count in range(20): 
   for index in range(n):      
      turtles[index].color(colors[index % n])
      turtles[index].right(random.randint(0,360))
      turtles[index].forward(random.randint(1,100))
      turtles[index].stamp()
