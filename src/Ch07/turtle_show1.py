# 코드 7-11 : 터틀 그래픽의 setup(), forward(), left(), bye() 메소드
## "으뜸 파이썬", p. 418

import turtle as t
t.setup(width = 400, height = 400)
t.forward(100)
t.left(90)
t.forward(100)
t.bye()        # 이 부분 때문에 윈도가 사라짐
