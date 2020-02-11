# 코드 7-24 : goto(), penup(), pendown() 메소드
## "으뜸 파이썬", p. 435

import turtle as t

t.goto(80, 100) # 1번
t.penup()        # 2번
t.goto(0, 100)   # 3번
t.pendown()      # 4번
t.goto(80, 0)   # 5번

t.done()
