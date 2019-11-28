
# 코드 10-12 : add() 메소드를 이용한 벡터의 덧셈


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
    
    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)

v3 = v1.add(v2)  # Vector2D의 add() 메소드 사용
print('v1.add(v2) =', v3)
