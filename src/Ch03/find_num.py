
# 코드 3-53 : 리스트에서 숫자를 찾는 순차 탐색 기능

nlist = [3, 2, 1, 4, 6, 5, 7]
n = int(input("찾을 숫자를 입력하시오 : "))

i = 0
while i < len(nlist):
    if nlist[i] == n:
        print("{}번째 입니다.".format(i+1))
        break
    print("탐색 중...")
    i += 1
