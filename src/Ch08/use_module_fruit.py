
# 코드 8-5 : 사용자 정의 모듈인 module_fruit를 import하여 사용하는 방법


import module_fruit   # module_fruit 모듈을 가져온다  

print(module_fruit.s) # module_fruit 모듈의 s라는 문자열 데이터를 사용
a = module_fruit.choose_fruit()  # module_fruit 모듈의 choose_fruit() 함수 사용
# a = choose_fruit()  # 에러 발생
print(a)
