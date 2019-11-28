
# 코드 10-15 : Circle 인스턴스와 클래스변수 PI


class Circle:
    PI = 3.1415   # 클래스변수
    def __init__(self, name, radius):
        self.__name = name      # 인스턴스변수
        self.__radius = radius  # 인스턴스변수

    # Circle 클래스의 변수 PI를 이용하여 면적을 구함
    def area(self):
        return Circle.PI * self.__radius ** 2


c1 = Circle('C1', 4)
print('c1의 면적:', c1.area())
c2 = Circle('C2', 6)
print('c2의 면적:', c2.area())
c3 = Circle('C3', 5)
print('c3의 면적:', c3.area())
