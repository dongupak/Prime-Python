
# 코드 4-23 : 직사각형과 원의 면적을 구하는 함수의 구현


def func(shape, width=1, height=1, radius=1):
    if shape == 0 : # shape 값이 0이면 사각형의 면적을 반환
        return width * height
    if shape == 1 : # shape 값이 1이면 원의 면적을 반환
        return 3.14 * radius ** 2

print("rect area =", func(0, width=10, height=2))
print("circle area =", func(1, radius=5))
