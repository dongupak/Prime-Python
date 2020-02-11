# 코드 10-11 : 맵 함수와 square() 호출을 이용한 제곱값 리스트 생성
## "으뜸 파이썬", p. 585

def square(x):
  return x ** 2

a = [1, 2, 3, 4, 5, 6, 7]
square_a = list(map(square, a)) # a의 각 항목에 대해 square 함수의 반환값을 적용
print(square_a)
