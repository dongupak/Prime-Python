# 코드 6-7 : 곱집합 함수 product_set()와 A, B 집합의 곱집합
## "으뜸 파이썬", p. 360

def product_set(set1, set2) :
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}     # 이중 for 루프를 이용한 곱집합
    return res

A = {1, 3}              # 집합 A의 원소
B = {2, 4}              # 집합 B의 원소
AxB = product_set(A,B)  # 집합 A와 B의 곱집합 AxB (A x B가 아님)
print('A =', A)
print('B =', B)
print('AxB =', AxB)     # A와 B의 곱집합을 출력
