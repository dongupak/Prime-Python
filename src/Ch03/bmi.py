
# 코드 3-18 : BMI를 구하여 저체중, 정상, 과체중, 비만, 고도 비만을 출력


height = float(input('키를 입력하세요(단위 m) : '))
weight = float(input('몸무게를 입력하세요(단위 kg) : '))

# bmi = 체중(kg) / 키(m)^2
bmi = weight / height**2

if bmi < 18.5:
    print('저체중') 
elif bmi < 25:
    print('정상')
elif bmi < 30:
    print('과체중')
elif bmi < 40:
    print('비만')
else:
    print('고도 비만')
