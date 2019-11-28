
# 코드 7-23 : pencolor() 메소드를 이용한 패턴 만들기


import turtle as t

colors = ['red', 'green', 'blue', 'orange']
for i in range(200):
    t.pencolor(colors[i % 4])
    t.forward(i)
    t.left(93)

t.done()
