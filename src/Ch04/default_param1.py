# 코드 4-20 : 디폴트 인자를 1개 사용한 div() 함수
## "으뜸 파이썬", p. 222

def div(a, b = 2):
    return a / b

print('div(4) =', div(4))
print('div(6, 3) =', div(6, 3))
