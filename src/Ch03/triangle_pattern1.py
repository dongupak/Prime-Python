
# 코드 3-42 : 삼각형 패턴을 출력하는 기능

n = 5
for i in range(n):
    for j in range(n - (i + 1)): # 공백을 출력함
        print(' ', end = '')
    for j in range(2 * i + 1):   # ‘+’를 출력함
        print('+', end = '')
    print()
