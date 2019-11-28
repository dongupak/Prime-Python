
try :
    f = open('my_hello.txt', 'w')  # 파일 열기
    f.write('Hello Python\n')    # hello.txt 파일에 쓰기
    f.close()
except PermissionError :
    print("파일 쓰기 오류");


