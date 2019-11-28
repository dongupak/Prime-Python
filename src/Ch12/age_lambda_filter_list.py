
# 코드 12-6 : 람다 함수를 이용한 간략화된 필터


ages = [34, 39, 20, 18, 13, 54]
adult_ages = list(filter(lambda x: x >= 19, ages))
print('성년 리스트 :', adult_ages)
