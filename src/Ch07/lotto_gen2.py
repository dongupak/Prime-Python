# 코드 7-9 : random 모듈을 이용한 로또 번호 만들기 2
## "으뜸 파이썬", p. 412

import random as rd
 
lotto_list = list(range(1, 46))         # 1부터 45까지 생성
lotto_list = rd.sample(lotto_list, 6)   # 임의의 값 6개를 추출(샘플링)
lotto_list.sort()                       # 선택된 번호를 정렬
print('이번 주의 추천 로또번호 :', lotto_list)
