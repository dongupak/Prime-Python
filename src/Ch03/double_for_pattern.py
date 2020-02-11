# 코드 3-37 : 이중 for 루프를 사용한 패턴 생성하기
## "으뜸 파이썬", p. 166

n = 7
for i in range(n):  # 외부 for 루프는 n번 수행, i는 0,1,2,3,4,5,6 까지 증가
    st = ''
    for j in  range(i):  # 내부 for 루프는 i번 수행
        st = st + ' '    # 공백을 i개 추가함
    print(st + '#')      # 공백 추가 후 '#'출력
