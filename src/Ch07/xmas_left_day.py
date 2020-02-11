# 코드 7-1 : datetime 모듈을 사용하여 크리스마스까지 남은 시간 구하기
## "으뜸 파이썬", p. 395

import datetime as dt

today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))

xMas = dt.datetime(2019, 12, 25)
time_gap = xMas - dt.datetime.now()

print('다음 크리스마스 까지는 {}일 {}시간 남았습니다.'.format( \
    time_gap.days,time_gap.seconds // 3600))
