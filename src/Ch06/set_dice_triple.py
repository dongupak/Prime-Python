# 코드 6-11 : 주사위 세 번 던져 나오는 모든 경우
## "으뜸 파이썬", p. 366

def tuple_sum(tup) :
    if isinstance(tup, float) or isinstance(tup, int) :
        return tup
    else:
        sum = 0
        for element in tup :
            sum += tuple_sum(element)
    return sum

sums = [tuple_sum(tup) for tup in cases_3times]
print(sums)

