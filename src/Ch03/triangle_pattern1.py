# 코드 3-41 : 삼각형 패턴을 출력하는 기능
## "으뜸 파이썬", p. 168

n = 5
for i in range(n):
    for j in range(n - (i + 1)): # 공백을 출력함
        print(' ', end = '')
    for j in range(2 * i + 1):   # ‘+’를 출력함
        print('+', end = '')
    print()
