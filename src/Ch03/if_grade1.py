# 코드 3-15 : 'A','B','C','D','F' 등급 계산을 위한 if 문
## "으뜸 파이썬", p. 138

score = int(input('점수를 입력하세요 : '))

if score >= 90 :                # 90 이상인 경우 ‘A’
    grade = 'A'
if score < 90 and score >= 80 : # 90 미만 80 이상인 경우 ‘B’
    grade = 'B'
if score < 80 and score >= 70 : # 80 미만 70 이상인 경우 ‘C’
    grade = 'C'
if score < 70 and score >= 60  : # 70 미만 60 이상인 경우 ‘D’
    grade = 'D'
if score < 60 :                  # 60 미만인 경우 ‘F’
    grade = 'F'

print('당신의 등급은 :', grade)
