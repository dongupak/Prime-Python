
# 코드 10-11 : 사용자 정의 Vector2D 클래스와 + 연산


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)

v3 = v1 + v2  # Vector2D의 + 연산이 정의되지 않았다
print('v1 + v2 = ',v3)
