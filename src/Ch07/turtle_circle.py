# 코드 7-20 : circle() 메소드를 이용한 여러 개의 원 그리기
## "으뜸 파이썬", p. 429

import turtle as t

t.setheading(90)     # 왼쪽 원 그리기
for i in range(1, 11):
    t.circle(10*i)    
    
t.setheading(270)     # 오른쪽 원 그리기
for i in range(1, 11):
    t.circle(10*i)    
t.done()
