import turtle
t = turtle.Turtle()
t.hideturtle()
colors = ["red", "green", "blue", "yellow"]

i = 0
for x in range(1, 200, 2):
       i += 1
       t.color(colors[i % 4])
       t.forward(x)
       t.left(94)
