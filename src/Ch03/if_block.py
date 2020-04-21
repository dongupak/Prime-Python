# 코드 3-12 : 외부 if-else 문과 내부 if-else 문의 사용
## "으뜸 파이썬", p. 131

num = -100

if num < 0:
    print(num, '은(는) 음수입니다.')
else:
    print(num, '은(는) 음수가 아닙니다.')
    
    # 짝수, 홀수는 음수가 아닐 때만 판별함
    if num % 2 == 0:
        print(num, '은(는) 짝수입니다.')
    else:
        print(num, '은(는) 홀수입니다.')
