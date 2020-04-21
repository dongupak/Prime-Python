# 코드 6-7 : 곱집합 함수 product_set()와 A, B 집합의 곱집합
## "으뜸 파이썬", p. 360

def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)} # 이중 for 루프를 이용한 곱집합
    return res

A = {1, 3}
B = {2, 4}

AxB = product_set(A, B)
print('A =', A)
print('B =', B)
print('AxB =', AxB)
