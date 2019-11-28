
# 코드 12-28 : OddCounter 클래스와 StopIteration 예외 생성기능


class OddCounter:
    def __init__(self, n = 1):
        self.n = n
  
    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 20:  # 반복자가 수행되는 조건
            t = self.n
            self.n += 2
            return t
        raise StopIteration  # 조건을 만족하지 않으면 StopIteration을 raise함

my_counter = OddCounter()
for x in my_counter:
    print(x, end = ' ')
