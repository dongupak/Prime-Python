
# 코드 12-10 : 맵 함수를 이용한 제곱값 리스트 생성


a = [1, 2, 3, 4, 5, 6, 7]
square_a = []
for n in a:
  square_a.append(n**2)  # n의 제곱을 square_a 리스트에 추가함
  
print(square_a)
