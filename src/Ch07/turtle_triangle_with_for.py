# 코드 7-17 : for 문을 사용한 삼각형 그리기
## "으뜸 파이썬", p. 425

import turtle as t

for _ in range(3):   # 아래의 기능을 세 번 반복
    t.forward(100)   # 터틀을 헤딩 방향으로 100 픽셀 이동
    t.left(120)      # 터틀의 헤딩 방향을 왼쪽으로 120도 회전

t.done()
