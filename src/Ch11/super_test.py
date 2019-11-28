
# 코드 11-3 : Person 클래스와 이 클래스를 상속 받은 Employee, Manager


class Person:    # 부모 클래스 Person
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    

# Person 클래스의 자식 클래스 
class Employee(Person):   
    def __init__(self, name, staff_id):        
        super().__init__(name)        
        self.staff_id = staff_id    # Person에 없는 추가적인 속성  
        
    def info(self):        
        return '종업원 : '+ super().get_name() + ', 사원번호 : '+str(self.staff_id)
    

worker = Employee('박동윤', 1111)
print(worker.info())
