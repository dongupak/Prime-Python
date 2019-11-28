
# 코드 11-5 : issubclass() 함수의 사용
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


print('Employee는 Person의 자식 클래스이다 :', issubclass(Employee, Person))
print('Manager는 Person의 자식 클래스이다 :', issubclass(Manager, Person))
print('str은 Person의 자식 클래스이다 :', issubclass(str, Person))
