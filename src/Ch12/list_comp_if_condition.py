
# 코드 12-22 : 리스트 축약 표현과 if 조건식을 이용한 필터링


n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
minus_list = [x for x in n_list if x < 0]
print('음수 리스트 :', minus_list)
