# 코드 6-11 : 주사위 세 번 던져 나오는 모든 경우
## "으뜸 파이썬", p. 366

def tuple_sum(tup) :                # tup내의 모든 항목의 합을 구하는 함수
    if isinstance(tup, int) :       # tup가 int 형이면 tup를 반환
        return tup
    else:
        accum = 0                   # tup 내의 모든 항목을 조회함
        for element in tup :
            accum += tuple_sum(element) # 이 항목의 합을 구하기 위한 재귀적 호출
    return accum

def product_set(set1, set2) :
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}     # 이중 for 루프를 이용한 곱집합
    return res

cases = {1, 2, 3, 4, 5, 6}
cases_2times = product_set(cases, cases)
cases_3times = product_set(cases, cases_2times)


sums = [tuple_sum(tup) for tup in cases_3times]
print(sums)                         # tup내의 모든 항목의 합을 리스트로 출력

