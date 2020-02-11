# 코드 7-28 : 체질량지수를 계산하기 위해 필요한 인터페이스 요소를 배치하는 코드
## "으뜸 파이썬", p. 446

from tkinter import *

window = Tk()
label = Label(window, text='체중(kg)과 키(cm)를 차례로 입력하세요.')
label.pack()

weight = Entry(window, width = 50)
weight.pack()

height = Entry(window, width = 50)
height.pack()

button = Button(window, text = 'BMI 계산')
button.pack()

result = Label(window, text='당신의 체질량 지수(BMI)는: ')
result.pack()

window.mainloop()
