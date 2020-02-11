# 코드 6-8 : 곱집합 함수를 이용한 집합의 세제곱 연산
## "으뜸 파이썬", p. 361

def product_set(set1, set2) :
    return {(i, j) for i in set1 for j in set2}

def exp(set, exponent) :
    res = set
    for _ in range(exponent-1) : 
        res = product_set(res, set)
    return res

A = {1,3}
A3 = exp(A, 3)
print(A3)
