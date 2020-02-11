# 코드 7-22 : 여러 개의 사각형 그리기
## "으뜸 파이썬", p. 431

import turtle as t

t.color('blue')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()       # 사각형 내부를 파란색으로 채워서 그리기

t.setheading(90)
t.color('red')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()       # 사각형 내부를 빨간색으로 채워서 그리기

t.done()
