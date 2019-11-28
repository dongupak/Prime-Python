
# 코드 8-6 : from - import 문을 사용하는 방법


# module_fruit 모듈의 s와 choose_fruit() 함수를 가져온다
from module_fruit import s, choose_fruit 

print(s)     # module_fruit 모듈의 s를 사용할 때 모듈 이름을 적을 필요가 없다
a = choose_fruit()
print(a)
