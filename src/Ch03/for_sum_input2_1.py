# 코드 3-49 : 1부터 n까지의 합을 구하는 코드로 while 문 내에서 입력문 사용
## "으뜸 파이썬", p. 175

n = -1
while n <= 0:  # 양수가 입력될 때 까지 input() 문을 반복 수행함
    n = int(input('합계를 구할 양의 정수를 입력하세요 : '))

s = 0

for i in range(1, n+1):
    s = s + i

print('1부터 {}까지의 합은 {}'.format(n, s))
