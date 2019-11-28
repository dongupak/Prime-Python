
# 코드 12-27 : OddCounter 클래스의 정의와 20보다 작은 홀수를 출력하는 방법


class OddCounter:
    def __init__(self, n = 1):
        self.n = n
  
    def __iter__(self):
        return self

    def __next__(self):
        t = self.n
        self.n += 2
        return t

my_counter = OddCounter()
for x in my_counter:
    if x > 20:   # 반복을 종료하는 조건 : x > 20
        break
    print(x, end = ' ')
