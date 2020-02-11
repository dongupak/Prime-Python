# 코드 4-14 : 매개변수를 사용하지 않고 외부 변수를 사용하는 경우
## "으뜸 파이썬", p. 215

def print_sum():
    result = a + b
    print('print_sum() 내부 :', a, '과', b, '의 합은', result, '입니다.')
    
a = 10
b = 20
print_sum()
result = a + b
print('print_sum() 외부 :', a, '과', b, '의 합은', result, '입니다.')
