import turtle as t
import math as m

t.penup()
t.goto(-400, 0)
t.pendown()
t.goto(400, 0)
t.penup()
t.goto(0, -400)
t.pendown()
t.goto(0, 400)
t.penup()
t.goto(0, 0)
t.pendown()
t.color('red')
t.width(4)
for d in range(1, 401, 30):
  t.goto(d, m.log(d))
  
