# 코드 8-12 : read() 메소드를 이용하여 지정된 문자 크기만큼 읽기
## "으뜸 파이썬", p. 494

f = open('hello.txt', 'r') # 파일을 연다.
s = f.read(5)              # hello.txt 파일의 다섯 문자를 읽는다.
print(s)                   # 파일의 내용을 출력한다.
f.close()                  # 파일을 닫는다.
