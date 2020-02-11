# 코드 9-14 : Circle 인스턴스와 속성 PI
## "으뜸 파이썬", p. 551

class Circle:
    def __init__(self, name, radius, PI):
        self.__name = name      # 인스턴스변수
        self.__radius = radius  # 인스턴스변수
        self.__PI = PI          # 인스턴스변수

    #  현재 인스턴스의 PI에 반지름**2 을 곱하여 면적을 구함
    def area(self):
        return self.__PI * self.__radius ** 2


c1 = Circle('C1', 4, 3.14)
print('c1의 면적:', c1.area())
c2 = Circle('C2', 6, 3.141)
print('c2의 면적:', c2.area())
c3 = Circle('C3', 5, 3.1415)
print('c3의 면적:', c3.area())
