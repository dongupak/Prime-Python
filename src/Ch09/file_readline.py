
# 코드 9-13 : readline() 메소드를 이용한 줄 단위 읽기와 출력하기

f = open('foo.txt','r')    # 파일 연다.
s = f.readline()           # 파일의 첫 번째 줄 'AAA'을 읽어온다
print(s, end = '')           # 이 줄을 출력한다.
s = f.readline()           # 파일의 두 번째 줄 'BBB'를 읽어온다
print(s, end = '')           # 이 줄을 출력한다.
f.close()                  # 파일을 닫는다.
