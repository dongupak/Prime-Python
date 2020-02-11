# 코드 6-4 : 튜플과 할당 연산자를 이용한 간단한 swap
## "으뜸 파이썬", p. 344

a = 100
b = 200
print('swap 이전 : a = ', a, 'b = ', b)
a, b = b, a
print('튜플을 사용한 swap 결과 : a = ', a, 'b = ', b)
