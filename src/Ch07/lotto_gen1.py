# 코드 7-8 : random 모듈을 이용한 로또 번호 만들기 1
## "으뜸 파이썬", p. 411

import random as rd
 
lotto_list = list(range(1, 46))  # 1부터 45까지 생성
rd.shuffle(lotto_list)       # 임의의 순서로 섞기
lotto_list = lotto_list[:6]  # 앞 부분 6개만 선택
lotto_list.sort()            # 선택된 번호를 정렬
print('이번 주의 추천 로또번호 :', lotto_list)
