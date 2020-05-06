# 코드 7-16 : forward() 명령과 left() 명령를 사용한 삼각형 그리기
## "으뜸 파이썬", p. 424

import turtle as t

t.shape("turtle")
t.forward(100)
t.left(120)      # 일반각을 사용합니다. 
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

t.done()
