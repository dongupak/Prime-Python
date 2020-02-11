# 코드 7-25 : 터틀 그래픽의 랜덤 플로팅
## "으뜸 파이썬", p. 436

import turtle as t
import random as rd

t.shape("circle")
d = 300
for _ in range(40):
    x = rd.randint(-d, d)
    y = rd.randint(-d, d)
    t.goto(x, y)
    
t.done()
