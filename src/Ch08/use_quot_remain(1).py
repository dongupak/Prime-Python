
# 코드 8-11 : use_quot_remain.py의 수정된 코드


import sys
sys.path.append('C:\\workspace') # 코드 내에서 모듈의 경로를 등록함
import quot_remain  # quot_remain 모듈을 가져온다

x = 22
y = 4
q, r = quot_remain.quot_remain(x, y)
print('{} / {}의 몫은 {}, 나머지는 {}'.format(x, y, q, r))
