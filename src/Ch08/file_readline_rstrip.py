# 코드 8-14 : readline() 메소드와 rstrip()을 이용한 줄 단위 읽기와 출력
## "으뜸 파이썬", p. 495

f = open('foo.txt','r')    # 'foo.txt' 파일을 연다.
s = f.readline().rstrip()  # 'AAA' 줄을 읽고 오른쪽 줄 바꿈 문자를 지움
print(s)                   # 이 줄을 출력한다.
s = f.readline().rstrip()  # 'BBB' 줄을 읽고 오른쪽 줄 바꿈 문자를 지움
print(s)                   # 이 줄을 출력한다.
f.close()                  # 파일을 닫는다.
