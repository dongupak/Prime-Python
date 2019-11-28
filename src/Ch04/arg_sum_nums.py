
# 코드 4-28 : 가변 인자를 가지는 함수를 이용한 합계 구하기

def sum_nums(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result
 
print(sum_nums(10, 20, 30))    # 10, 20, 30 인자들의 합을 출력
print(sum_nums(10, 20, 30, 40, 50))    # 10, 20, 30, 40, 50 인자들의 합을 출력
