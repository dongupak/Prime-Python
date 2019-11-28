
# 코드 12-13 : reduce() 함수를 사용한 멤버 덧셈


from functools import reduce
a = [1, 2, 3, 4]
n = reduce(lambda x, y: x + y, a)
print(n)
