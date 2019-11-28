
# 코드 6-6 : 원의 면적과 둘레를 튜플 형식으로 반환하는 함수


def area_and_circum(r):  # 원의 면적과 둘레 구하기
    area = 3.14 * r ** 2
    circum = 2 * 3.14 * r
    return area, circum   # 튜플을 반환함 – 반환값 (area, circum)

radius = 4
a, c = area_and_circum(radius)   # 반환받은 튜플을 언패킹함
print('반지름 {}인 원의 면적과 둘레 : {}, {}'.format(radius, a, c))
