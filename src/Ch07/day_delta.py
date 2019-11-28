
# 코드 7-2 : 100일 후, 100일 전 날짜 구하기


import datetime as dt

print('오늘 =', dt.datetime.now())        # 현재시간을 구한다

hundred = dt.timedelta(days = 100)        # 100일 경과시간
plus100day = dt.datetime.now() + hundred  # 현재 시간에서 100일 경과시간을 더함
print('100일 후 =', plus100day)

minus100day = dt.datetime.now() - hundred  # 현재 시간에서 100일 경과시간을 뺌
print('100일 전 =', minus100day)
