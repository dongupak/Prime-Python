# 코드 3-16 : 'A','B','C','D','F' 등급 계산을 위한 복합 if 문
## "으뜸 파이썬", p. 140

score = int(input('점수를 입력하세요 : '))

if score >= 90:       # 90 이상인 경우 ‘A’
    grade = 'A'

else:
    if score >= 80 :  # 90 미만 80 이상인 경우 ‘B’

        grade = 'B'
    else:
        if score >= 70:  # 80 미만 70 이상인 경우 ‘C’
            grade = 'C'
        else:
            if score >= 60:  # 70 미만 60 이상인 경우 ‘D’
                grade = 'D'
            else:            # 60 미만인 경우 ‘F’
                grade = 'F'

                
print('당신의 등급은 :', grade)
