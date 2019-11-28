
# 코드 9-1 : try-except 구문을 이용한 예외처리


try:
    a, b = input('두 수를 입력하시오: ').split()
    result = int(a) / int(b)
    print('{}/{} = {}'.format(a, b, result))
except :
    print('수가 정확한지 확인하세요.')
