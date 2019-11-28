
# 코드 11-9 : Person 클래스의 __eq__() 메소드 오버라이딩


class Person:
    def __init__(self, name):
        self.name = name
        
    def __eq__(self, obj):  # == 연산자의 기능을 재정의 함
        return self.name == obj.name
    
person_a = Person('이순신')
person_b = Person('이순신')

print('== 연산자로 person_a와 person_b를 비교합니다.')
if person_a == person_b:
  print('두 인스턴스는 같습니다.')
else:
  print('두 인스턴스는 다릅니다.')
