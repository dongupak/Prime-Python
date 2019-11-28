
# 코드 7-21 : color(), begin_fill(), end_fill()을 이용한 색상 사각형 그리기 


import turtle as t

t.color('blue')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.done()
