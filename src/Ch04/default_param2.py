
# 코드 4-21 : 매개변수에 디폴트 값을 2개 사용한 div() 함수


def div(a = 1, b = 2):
    return a / b

print('div() =', div())
print('div(4) =', div(4))
print('div(6, 3) =', div(6, 3))
