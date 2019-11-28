
# 코드 9-5 : try-except 문을 사용한 구체적인 예외처리


try:
#    b = 2 / 0
    a = 1 + 'hundred'
except ZeroDivisionError:
    print('0으로 나누는 오류')
except TypeError:
    print('지원되지 않은 연산자를 사용하는 오류')
