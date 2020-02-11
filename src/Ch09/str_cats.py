# 코드 9-5 : __str__ 메소드와 print() 함수에서 적용하기
## "으뜸 파이썬", p. 537

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    # Cat 객체의 문자열 표현방식
    def __str__(self):
        return 'Cat(name = '+self.name+', color = '+self.color+')'


nabi = Cat('나비', '검정색') # nabi 인스턴스 생성
nero = Cat('네로', '흰색')  # nero 인스턴스 생성

print(nabi)
print(nero)
