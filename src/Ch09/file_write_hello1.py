
# 코드 9-20 : 파일 열기와 쓰기, 파일 닫기의 표현 1


f = open('hello.txt', 'w')  # 파일 열기
f.write('Hello World!')     # hello.txt 파일에 쓰기
f.close()                   # 파일을 닫는다.
