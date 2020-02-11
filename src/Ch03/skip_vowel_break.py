# 코드 3-50 : break를 사용하여 모음이 나타나면 즉시 반복문을 종료하는 기능
## "으뜸 파이썬", p. 177

st = 'Programming'

# 자음이 나타나는 동안만 출력하는 기능
for ch in st:
    if ch in ['a','e','i','o','u']:
        break   # 모음일 경우 반복문을 종료한다.
    print(ch)

print('The end')
