
# 코드 9-10 : 파일 열기와 쓰기, 파일 닫기의 표현


f = open('hello.txt', 'w')  # 1) 파일을 연다.
f.write('Hello World!')     # 2) hello.txt 파일에 문자를 쓴다.
f.close()                   # 3) 파일을 닫는다.
