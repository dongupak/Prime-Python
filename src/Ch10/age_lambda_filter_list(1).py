# 코드 10-19 : list() 함수, filter() 함수, 람다 함수를 이용한 필터링
## "으뜸 파이썬", p. 594

ages = [34, 39, 20, 18, 13, 54]
adult_ages = list(filter(lambda x: x >= 19, ages))
print('성년 리스트 :', adult_ages)
