
# 코드 3-48 : while 반복문을 이용한 가위, 바위, 보 선택하기


selected = None
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에서 선택하세요> ')

print('선택한 값은:', selected)
