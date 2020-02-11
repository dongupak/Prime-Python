# 코드 10-7 : 람다 함수를 이용한 음수 값 추출기능 1
## "으뜸 파이썬", p. 581

def minus_func(n):   # n이 음수이면 True, 그렇지 않으면 False를 반환
    if n < 0 :
        return True
    else:
        return False

n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
minus_list = []     # 음수를 저장할 리스트
for n in filter(minus_func, n_list):
    minus_list.append(n)
print('음수 리스트 :', minus_list)
