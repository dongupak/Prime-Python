
# 코드 8-9 : 몫과 나머지를 반환하는 함수 quot_remain()을 가진 파일


def quot_remain(m, n):   # m을 n으로 나눈 몫 q와 나머지 r을 반환하는 함수
    q = m // n
    r = m % n  
    return q, r     # q, r 튜플을 반환
