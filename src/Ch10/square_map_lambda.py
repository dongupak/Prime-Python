# 코드 10-12 : 맵 함수와 람다 함수를 이용한 제곱값 리스트 생성
## "으뜸 파이썬", p. 585

a = [1, 2, 3, 4, 5, 6, 7]
square_a = list(map(lambda x: x**2, a))
print(square_a)
