# 코드 7-27 : Tkinter를 이용한 간단한 실습 코드
## "으뜸 파이썬", p. 443

from tkinter import *

def change_label():
    if label.cget("text") == '헬로 파이썬' :
        label.config(text = '안녕 파이썬')
        label.config(bg = 'cyan')
    else:
        label.config(text = '헬로 파이썬')
        label.config(bg = 'yellow')
    
window = Tk()
label = Label(window, text = '헬로 파이썬', bg = 'yellow')
label.pack()
btn = Button(window, text = '클릭하면 문자가 변경됨', fg = 'blue', \
             command = change_label)
btn.pack()

window.mainloop()
