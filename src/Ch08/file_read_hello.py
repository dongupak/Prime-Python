# 코드 8-11 : 파일 열기와 읽기, 파일 닫기의 표현
## "으뜸 파이썬", p. 493

f = open('hello.txt', 'r') # 파일을 연다.
s = f.read()               # hello.txt 파일을 읽는다.
print(s)                   # 파일의 내용을 출력한다.
f.close()                  # 파일을 닫는다.
