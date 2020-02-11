# 코드 4-26 : 가변 인자를 가지는 함수의 정의와 호출
## "으뜸 파이썬", p. 232

def greet(*names):
   for name in names:
       print('안녕하세요', name, '씨')

greet('홍길동', '양만춘', '이순신') # 인자가 3개
greet('James', 'Thomas') # 인자가 2개
