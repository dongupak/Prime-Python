
# 코드 4-15 : 함수 외부에서 정의된 값을 함수 내부에서 변경하는 경우

 
def print_sum():
    a = 100
    b = 200
    result = a + b
    print('print_sum() 내부 :', a, '과', b, '의 합은', result, '입니다.')
    
a = 10
b = 20
print_sum()
