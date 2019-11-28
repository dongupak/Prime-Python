
# 코드 10-7 : set_age() 메소드를 통해서 age 값을 할당하기


class Cat:
    def __init__(self, name, age):
        self.__name = name  # Cat 클래스의 인스턴스변수를 감추는 역할
        self.__age = age
    
    # Cat의 문자열 표현방식
    def __str__(self):
        return 'Cat(name = '+self.__name+', age = '+str(self.__age)+')'

    # self.__age를 외부에서 자유롭게 접근하는 것을 제한하고 음수가 되지 않도록 함
    def set_age(self, age):  
        if age > 0:
            self.__age = age
            
    def get_age(self):
        return self.__age

nabi = Cat('나비', 3) # nabi 인스턴스 생성
print(nabi)
nabi.set_age(4)   # set_age() 메소드를 통해서 age에 접근
nabi.set_age(-5)  # set_age() 메소드를 통해서 age가 음수가 되지 않도록 함
print(nabi)
