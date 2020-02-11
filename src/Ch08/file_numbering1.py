# 코드 8-18 : 사용자로부터 입력받은 파일을 번호를 붙여서 출력하기
## "으뜸 파이썬", p. 500

fname = input('입력할 파일의 이름 : ')
f = open(fname, 'r')  # 파일 열기
n = 1                 # 줄 번호를 출력하기 위한 변수 
l = f.readline()
while l :      # 읽어들일 줄이 있으면 반복 수행함
    print('{:3d}: {}'.format(n, l), end = '') # 줄 번호와 내용을 출력
    n += 1                                 # 줄 번호를 증가시킴
    l = f.readline()

f.close()
