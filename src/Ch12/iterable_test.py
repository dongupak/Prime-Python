
# 코드 12-25 : 리스트와 튜플, 정수 값을 반복자 객체로 변환시키기


# 리스트가 반복 가능 객체인가 검사
try:
    l = [10, 20, 30]
    iterator = iter(l)
except TypeError:
    print('list는 iterable 객체가 아닙니다.')
else:
    print('list는 iterable 객체입니다.')

# 튜플이 반복 가능 객체인가 검사
try:
    t = ('홍길동', 22, 79.7)
    iterator = iter(t)
except TypeError:
    print('tuple은 iterable 객체가 아닙니다.')
else:
    print('tuple은 iterable 객체입니다.')

# 정수형이 반복 가능 객체인가 검사
try:
    n = 100
    iterator = iter(n)
except TypeError:
    print('n은 iterable 객체가 아닙니다.')
else:
    print('n은 iterable 객체입니다.')
