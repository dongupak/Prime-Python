# 코드 3-1 : 순차적 실행 구조를 이용한 변수의 덧셈
## "으뜸 파이썬", p. 114

num = 100
print('num = ', num)  # 100이 출력됨
num = num + 100
print('num = ', num)  # num에 100이 더해져 200이 출력됨
num = num + 100
print('num = ', num)  # num에 다시 100이 더해져 300이 출력됨
