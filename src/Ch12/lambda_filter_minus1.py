
# 코드 12-8 : 람다 함수를 이용한 음수 값 추출기능 2


n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
minus_list = []

for n in filter(lambda x: x < 0, n_list):
    minus_list.append(n)

print('음수 리스트 :', minus_list)
