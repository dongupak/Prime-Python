
# 코드 3-17 : if-elif-else 문으로 구성된 등급계산기

score = int(input('점수를 입력하세요 : '))

if score >= 90:       # 90 이상인 경우 'A'
    grade = 'A'
elif score >= 80:     # 'A'가 아닌 경우, 80 이상이면 'B'
    grade = 'B'
elif score >= 70:     # 'B'도 아닌 경우, 70 이상이면 'C'
    grade = 'C'
elif score >= 60:     # 'C'도 아닌 경우, 60 이상이면 'D'
    grade = 'D'
else:                 # 그 외의 경우 'F'
    grade = 'F'
    
print('당신의 등급은 :', grade)
