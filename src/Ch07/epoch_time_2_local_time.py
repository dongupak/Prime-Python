# 코드 7-3 : time 모듈의 유닉스 시간을 현재 지역 시간으로 표시하기
## "으뜸 파이썬", p. 399

import time

unix_timestamp = time.time()
local_time = time.localtime(unix_timestamp)
print(time.strftime('%Y-%m-%d %H:%M:%S', local_time))
