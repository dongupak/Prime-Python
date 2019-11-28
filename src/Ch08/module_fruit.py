
# 코드 8-4 : choose_fruit() 함수를 가진 module_fruit.py 스크립트 파일


import random   # random 모듈을 이 스트립트 파일에 가져온다

s = '오늘 먹을 과일을 골라볼까?'  # 문자열 객체를 만들고 이를 s가 참조

def choose_fruit():     # 랜덤하게 과일을 선택하는 함수
    fruits = ['apple', 'orange', 'banana', 'melon']
    f = random.choice(fruits)
    return f
