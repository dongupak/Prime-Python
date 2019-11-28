
# 코드 6-10 : 주사위 두 번 던져 나오는 모든 경우에 대해 눈의 합 구하기


def product_set(set1, set2) :
    return {(i, j) for i in set1 for j in set2}

cases = { 1, 2, 3, 4, 5, 6 }
cases_2times = product_set(cases, cases)

sum_set = { sum(tup) for tup in cases_2times }
print('sum_set =', sum_set)
sum_list = [ sum(tup) for tup in cases_2times ]
print('sum_list =', sum_list)
