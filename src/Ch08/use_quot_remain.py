
#코드 8-10 : 사용자 정의 모듈인 quot_remain을 import하여 몫과 나머지 구하기


import quot_remain      # 사용자 정의 모듈 quot_remain을 가져옴

x = 22
y = 4
q, r = quot_remain.quot_remain(x, y) # 사용자 정의 모듈의 quot_remain() 함수 호출
print('{} / {}의 몫은 {}, 나머지는 {}'.format(x, y, q, r))
