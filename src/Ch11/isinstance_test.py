
# 코드 11-4 : isinstance() 함수의 사용

# Employee와 Manager의 부모 클래스
class Person:
    def __init__(self, name):
        self.name = name        
    def get_name(self):
        return self.name


class Employee(Person):    # Person 클래스의 자식 클래스 
    def __init__(self, name, staff_id):        
        Person.__init__(self, name)        
        self.staff_id = staff_id    
    def info(self):        
        return '종업원 : ' + self.get_name() + ', 사원번호 : '+ str(self.staff_id)
    

class Manager(Person):   # Person 클래스의 자식 클래스 
    def __init__(self, name, position):
        Person.__init__(self, name)
        self.position = position            
    def info(self):
        return '고용주 : ' + self.get_name() + ', 직책 : ' + str(self.position)
    

worker1 = Employee('박동윤', 1111)
worker2 = Employee('흥승주', 2222)
cfo = Manager('박동민', 'CFO')

print(worker1.info())
print(worker2.info())
print(cfo.info())

        
print('worker1는 Employee의 인스턴스이다 :', isinstance(worker1, Employee))
print('worker1는 Manager의 인스턴스이다 :', isinstance(worker1, Manager))
print('worker1는 Person의 인스턴스이다 :', isinstance(worker1, Person))

print('cfo는 Employee의 인스턴스이다 :', isinstance(cfo, Employee))
print('cfo는 Manager의 인스턴스이다 :', isinstance(cfo, Manager))
print('cfo는 Person의 인스턴스이다 :', isinstance(cfo, Person))
