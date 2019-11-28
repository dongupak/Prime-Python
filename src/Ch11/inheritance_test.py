
# 코드 11-2 : Person 클래스와 이를 상속받는 Employee 클래스


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
