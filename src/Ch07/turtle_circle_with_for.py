# 코드 7-19 : forward(), left() 메소드를 사용한 원 그리기
## "으뜸 파이썬", p. 427

import turtle as t

n = 4
length = 50
for i in range(n):
    t.left(360/n)
    t.forward(length)
    
t.done()
