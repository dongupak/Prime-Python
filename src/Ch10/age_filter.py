# 코드 10-4 : 19 이상의 값을 반환하는 adult_func() 함수와 필터 함수의 사용
## "으뜸 파이썬", p. 578

def adult_func(n):   # 19세 이상의 값이 들어오면 True, 그렇지 않으면 False를 반환
    if n >= 19:
        return True
    else:
        return False

ages = [34, 39, 20, 18, 13, 54]
print('성년 리스트 :')
for a in filter(adult_func, ages):  # filter() 함수를 사용한 ages의 필터링
    print(a, end = ' ')
