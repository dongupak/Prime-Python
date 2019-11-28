
# 코드 6-1 : 리스트의 항목 삭제와 lst[1] 항목의 변화 여부


lst = [11, 22, 33, 44, 55]
print('pop(0) 이전 :', lst)
print('pop(0) 이전 lst[1] = ', lst[1])
lst.pop(0)   # 인덱스 0을 이용하여 리스트의 첫 항목을 삭제한다
print('pop(0) 이후 :', lst)
print('pop(0) 이후 lst[1] = ', lst[1])
