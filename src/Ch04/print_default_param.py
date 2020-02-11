# 코드 4-19 : 디폴트 값을 가지는 print_star() 함수
## "으뜸 파이썬", p. 221

def print_star(n = 1):  # 매개변수 n은 디폴트 값 1을 가짐
    for _ in range(n):
        print('************************')

print_star() # 인자가 없더라도 에러없이 수행됨
