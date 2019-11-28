
# 코드 5-5 : in 연산자를 이용한 안전한 원소 삭제


n_list = [11, 22, 33, 44, 55, 66]
if (55 in n_list) :  # 리스트의 요소로 55가 있을 경우
    n_list.remove(55)  # 리스트에서 55를 삭제함
    
if (88 in n_list) :  # 리스트의 요소로 88이 있을 경우
    n_list.remove(88)  # 리스트에서 88을 삭제함

print(n_list)
