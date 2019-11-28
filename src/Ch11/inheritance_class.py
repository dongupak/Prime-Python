
# 코드 11-1 : 클래스와 상속의 구현


class A :
    PI = 3.14
    
class B(A):
    pass

a = A()  # A 클래스의 인스턴스 a 생성
b = B()  # B 클래스의 인스턴스 b 생성
print('a.PI =', a.PI)
print('b.PI =', b.PI)  # b는 부모 클래스의 속성에 접근 가능함
