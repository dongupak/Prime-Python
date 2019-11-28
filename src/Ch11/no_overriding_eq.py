
# 코드 11-8 : Person 클래스의 __eq__() 메소드 오버라이딩 하기 전


class Person:
    def __init__(self, name):
        self.name = name
    
person_a = Person('이순신')
person_b = Person('이순신')

print('== 연산자로 person_a와 person_b를 비교합니다.')
if person_a == person_b:
  print('두 인스턴스는 다릅니다.')
else:
  print('두 인스턴스는 같습니다.')
