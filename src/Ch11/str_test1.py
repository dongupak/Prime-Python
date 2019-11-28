
# 코드 11-6 : Person 객체의 출력(__str__() 생성 이전)


class Person:
    def __init__(self, name):
        self.name = name
    
person = Person('이순신')
print(person)
