# 코드 7-29 : 체질량지수를 계산기
## "으뜸 파이썬", p. 447

from tkinter import *

def bmi_compute():     # 체질량 계산 함수
    w = float(weight.get())         # 입력된 체중 값을 실수로 변환
    h = float(height.get())/100.0   # cm로 입력된 키를 m 단위 환산
    bmi = w/(h*h)      # 체질량 값을 계산함
    answer = '당신의 체질량 지수(BMI)는: {:4.2f}'.format(bmi)
    result.config(text=answer)   # 체질량 값을 result 레이블에 적용
    
window = Tk()
label = Label(window, text='체중(kg)과 키(cm)를 차례로 입력하세요.')
label.pack()

weight = Entry(window, width = 50)
weight.pack()

height = Entry(window, width = 50)
height.pack()

button = Button(window, text = 'BMI 계산', command=bmi_compute)
button.pack()

result = Label(window, text='당신의 체질량 지수(BMI)는: ')
result.pack()

window.mainloop()
