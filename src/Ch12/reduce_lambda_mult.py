
# 코드 12-14 : 람다 함수와 리듀스를 이용한 축약



from functools import reduce
a = [1, 2, 3, 4]
n = reduce(lambda x, y: x * y, a)
print(n)
