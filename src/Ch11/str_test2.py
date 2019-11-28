
# 코드 11-7 : Person 클래스의 __str__() 메소드의 선언과 사용


class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Person의 이름은 {}입니다'.format(self.name)
    
person = Person('이순신')
print(person)
