# 코드 7-6 : 의사 랜덤 함수를 이용한 난수 만들기
## "으뜸 파이썬", p. 409

def pseudo_rand(x):
    a = 1103515245
    b = 12345
    m = 2 ** 31
    new_x = (a * x + b) % m
    return new_x

x = pseudo_rand(100)
print(x)
x = pseudo_rand(101)
print(x) 
x = pseudo_rand(32)
print(x) 
x = pseudo_rand(45)
print(x) 
