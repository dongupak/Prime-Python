
# 코드 3-43 : 삼각형 패턴을 출력하는 기능을 가진 짧은 코드


n = 5
for i in range(n):
    print(' ' * (n - (i + 1)), end = '')
    print('+' * (2 * i + 1))
