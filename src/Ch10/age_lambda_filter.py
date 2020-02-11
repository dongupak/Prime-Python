# 코드 10-5 : 람다 함수를 이용한 간략화된 필터
## "으뜸 파이썬", p. 579

ages = [34, 39, 20, 18, 13, 54]

print('성년 리스트 :')
for a in filter(lambda x: x >= 19, ages): # filter() 함수를 사용한 ages의 필터
    print(a, end = ' ')
