
# 코드 6-3 : 임시변수 temp를 이용한 값의 교환


a = 100
b = 200
print('swap 이전 : a = ', a, 'b = ', b)
temp = a
a = b
b = temp
print('swap 이후 : a = ', a, 'b = ', b)
