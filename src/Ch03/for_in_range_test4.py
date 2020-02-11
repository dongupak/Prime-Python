# 코드 3-24 : range() 함수를 이용한 for 문의 제어와 간격값 사용법
## "으뜸 파이썬", p. 153

# 표현식 1 : 2에서 5-1까지 연속값 2, 3, 4 출력
for i in range(2, 5):
    print(i, end = ' ')
print()

# 표현식 2 : 간격 값을 사용하여 0, 2, 4, 6, 8 출력
for i in range(0, 10, 2):
    print(i, end = ' ')
print()

# 표현식 3 : 음수 간격 값 사용, -2, -4, -6, -8 출력
for i in range(-2, -10, -2):
    print(i, end = ' ')
print()
