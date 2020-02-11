# 코드 3-14 : 윤년을 판별하기 위한 코드
## "으뜸 파이썬", p. 137

# 윤년 판별하기
year = int(input('연도를 입력하세요: '))
is_leap_year = ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0))
print(year, '년은 윤년입니까?', is_leap_year)
