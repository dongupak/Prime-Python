# 코드 4-6 : 매개변수를 사용하여 지정된 문자를 인자 값만큼 반복 출력하기
## "으뜸 파이썬", p. 205

def print_hello(n):             # 매개변수를 이용한 반복 출력
    print('Hello ' * n)

    
print('Hello를 두 번 출력합니다.')
print_hello(2)
print('Hello를 세 번 출력합니다.')
print_hello(3)
print('Hello를 네 번 출력합니다.')
print_hello(4)
