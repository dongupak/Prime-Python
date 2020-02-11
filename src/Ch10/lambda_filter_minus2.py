# 코드 10-9 : 람다 함수를 이용한 음수 값 추출기능 3
## "으뜸 파이썬", p. 582

n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
minus_list = list(filter(lambda x: x < 0, n_list))
print('음수 리스트 :', minus_list)
