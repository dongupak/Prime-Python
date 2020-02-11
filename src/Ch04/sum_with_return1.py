# 코드 4-11 : 두 값의 합을 반환하는 get_sum() 함수와 return 문의 사용1
## "으뜸 파이썬", p. 212

def get_sum(a, b):
    # 두 수의 합을 반환하는 함수
    result = a + b
    return result           # return 문을 사용하여 result를 반환

n1 = get_sum(10, 20)
print('10과 20의 합 =', n1)

n2 = get_sum(100, 200)
print('100과 200의 합 =', n2)
