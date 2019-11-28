
# 코드 3-27 : 누적 덧셈의 중간 결과 출력하기

s = 0
for i in range(1, 11):
    s = s + i
    print('i = {}, s = {}'.format(i, s) )
    
print('1에서 10까지의 합:', s)
