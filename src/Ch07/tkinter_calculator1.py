# 코드 7-30 : Tkinter를 이용한 계산기 외형 만들기
## "으뜸 파이썬", p. 451

from tkinter import *
 
window = Tk()
window.title("계산기")
window.geometry('350x200')

Label(window, text = "숫자 1").grid(column = 0, row = 0)
Label(window, text = "숫자 2").grid(column = 0, row = 1)
res_label = Label(window, text = "결과 :")
res_label.grid(column = 0, row = 2)
 
num1 = Entry(window, width = 10)
num2 = Entry(window, width = 10)
num1.grid(column = 1, row = 0)
num2.grid(column = 1, row = 1)

btn_plus = Button(window, text = "+", command = None)
btn_minus = Button(window, text = "-", command = None)
btn_mult = Button(window, text = "*", command = None)
btn_div = Button(window, text = "/", command = None)

btn_plus.grid(column = 4, row = 1)
btn_minus.grid(column = 5, row = 1)
btn_mult.grid(column = 6, row = 1)
btn_div.grid(column = 7, row = 1)

window.mainloop()
