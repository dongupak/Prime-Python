
# 코드 8-20 : C:\workspace 디렉토리 아래의 pkg_test1.py


import mypkg.calc.add
import mypkg.calc.sub
import mypkg.shape.circle
import mypkg.shape.triangle
import mypkg.shape.rectangle

mypkg.calc.add.add(200, 100)
mypkg.calc.sub.sub(200, 100)

mypkg.shape.circle.circle(10)
print('원주율은 {} 입니다.'.format(mypkg.shape.circle.PI))

mypkg.shape.triangle.triangle(10, 20)
mypkg.shape.rectangle.rectangle(10, 20)
