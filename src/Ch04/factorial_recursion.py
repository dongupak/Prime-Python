
# 코드 4-29 : 재귀함수를 이용하여 정의한 팩토리얼


def factorial(n):    # n!의 재귀적 구현
    if n <= 1 :      # 종료조건이 반드시 필요하다
        return 1
    else :
        return n * factorial(n-1)   # n * (n-1)! 정의에 따른 구현
 
n = 5
print('{}! = {}'.format(n, factorial(5)))
