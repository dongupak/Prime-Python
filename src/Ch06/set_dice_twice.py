# 코드 6-9 : 주사위 두 번 던져 얻는 경우를 모두 구하기
## "으뜸 파이썬", p. 362

def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)} # 이중 for 루프를 이용한 곱집합
    return res

cases = { 1, 2, 3, 4, 5, 6}
cases_2times = product_set(cases, cases)
print(cases_2times)
