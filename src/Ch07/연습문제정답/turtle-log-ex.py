import turtle as t
import math as m

for d in range(1, 301, 30):
  print('log({:2d}) = {:6.3f}'.format(d, m.log(d)))
  t.goto(d, m.log(d))
  
