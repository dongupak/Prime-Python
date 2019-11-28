
# 코드 6-5 : 튜플의 항목 값을 리스트를 이용하여 변경


t_fruits = ('apple', 'orange', 'water melon')
print('변경 전 :', t_fruits)
f_list = list(t_fruits) # 튜플을 리스트로 변환
f_list[1] = 'kiwi'  # 리스트의 두 번째 항목 값을 ‘kiwi'로 변경함
t_fruits = tuple(f_list) # 리스트를 튜플로 변환
print('변경 후 :', t_fruits)
