# 코드 9-17 : 언더스코어로 시작하는 인스턴스변수의 값 알아보기
## "으뜸 파이썬", p. 555

class Circle:
    PI = 3.14
    def __init__(self, name, radius):
        self.__name = name
        self.__radius = radius

c1 = Circle('C1',4)
print('c1의 속성들:', c1.__dict__)

# __dic__[key] 형식으로 value를 얻을 수 있음
print('c1의 __name 변수값:', c1.__dict__['_Circle__name'])
print('c1의 __radius 변수값:', c1.__dict__['_Circle__radius'])
