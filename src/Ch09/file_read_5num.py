
# 코드 9-17 : 사용자로부터 입력받은 정수 저장


f = open('data5.txt','r')  # 읽기 모드로 파일 열기
su = 0
for _ in range(5):
    n = int(f.readline())  # data5.txt 파일의 한 줄 내의 숫자를 읽어서
    su += n                # su에 누적해서 더한다
# 합과 평균을 출력
print('다섯 숫자의 합 = {}, 평균 = {}'.format(su, su/5))
f.close()                 # 파일을 닫는다.
