# 코드 4-16 : 함수 내부에서 값을 변경하고, 그 값을 외부에서 확인하기
## "으뜸 파이썬", p. 217

def print_sum():
    a = 100
    b = 200
    result = a + b
    print('print_sum() 내부 :', a, '과', b, '의 합은', result, '입니다.')
    
a = 10
b = 20
print_sum()
result = a + b
print('print_sum() 외부 :', a, '과', b, '의 합은', result, '입니다.')
