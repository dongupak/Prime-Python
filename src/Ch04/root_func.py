# 코드 4-13 : 두 개의 값을 튜플로 반환하는 방법과 전달 받는 방법
## "으뜸 파이썬", p. 214

def get_root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return r1, r2

# 함수 호출시 인자를 상수 값을 사용함
# result1, result2를 이용해서 결과 값을 반환 받아온다.
result1, result2 = get_root(1, 2, -8)
print('해는', result1, '또는', result2)
