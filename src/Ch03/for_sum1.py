
# 코드 3-34 : 리스트 항목내 정수 값들의 누적 덧셈

numbers = [10, 20, 30, 40, 50]

s = 0
for n in numbers:
    s = s + n

print('리스트 항목 값의 합 :', s)
