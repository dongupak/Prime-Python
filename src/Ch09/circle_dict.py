# 코드 9-16 : __dict__ 속성을 이용한 인스턴스변수와 값 알아보기
## "으뜸 파이썬", p. 554

class Circle:
    PI = 3.14
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

c1 = Circle('C1',4)
print('c1의 속성들:', c1.__dict__)
# __dic__[key] 형식으로 value를 얻을 수 있음
print('c1의 name 변수 값:', c1.__dict__['name'])
print('c1의 radius 변수 값:', c1.__dict__['radius'])
