# 코드 8-22 : 파일 열기와 쓰기, 파일 닫기의 표현 3
## "으뜸 파이썬", p. 506

with open('hello.txt', 'w') as f: # 파일 열기와 닫기를 자동 수행함
    f.write('Hello World!')    # hello.txt 파일에 쓰기
