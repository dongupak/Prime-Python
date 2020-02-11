# 코드 8-21 : 파일 열기와 쓰기, 파일 닫기의 표현 2
## "으뜸 파이썬", p. 505

f = open('hello.txt', 'w')  # 파일 열기
try:
    f.write('Hello World!')    # hello.txt 파일에 쓰기
finally:
    f.close()                  # 파일을 닫는다.
