# 코드 10-21 : list() 함수, fliter() 함수, 람다 함수를 이용한 필터링
## "으뜸 파이썬", p. 595

n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
minus_list = list(filter(lambda x: x < 0, n_list))
print('음수 리스트 :', minus_list)
