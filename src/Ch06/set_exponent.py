# 코드 6-8 : 곱집합 함수를 이용한 집합의 세제곱 연산
## "으뜸 파이썬", p. 361

def product_set(set1, set2) :
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)}     # 이중 for 루프를 이용한 곱집합
    return res

def exp(input_set, exponent) :
    res = input_set
    for _ in range(exponent-1) : 
        res = product_set(res, input_set)
    return res

A = {1,3}
A3 = exp(A, 3)          # 집합 A에 대하여 거듭제곱을 3회 수행함
print(A3)
