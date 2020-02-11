# 코드 9-6 : nabi.age에 직접 값을 할당하기
## "으뜸 파이썬", p. 540

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Cat 객체의 문자열 표현방식
    def __str__(self):
        return 'Cat(name = '+self.name+', age = '+str(self.age)+')'


nabi = Cat('나비', 3)   # nabi 인스턴스 생성
print(nabi)
nabi.age = 4
nabi.age = -5
print(nabi)
