
# 코드 12-26 : OddCounter 클래스의 정의와 객체 생성


class OddCounter:
    ''' 1부터 증가하는 홀수를 반환하는 클래스 '''
    def __init__(self, n = 1):  # 초기화 메소드 n을 1로 둔다
        self.n = n
  
    def __iter__(self):  # 반복자는 __iter__() 함수를 가져야 함
        return self

    def __next__(self):  # 반복자는 __next__() 함수를 가져야 함
        t = self.n      # self.n을 임시 변수 t에 저장해 두고
        self.n += 2     # self.n을 2증가시킨다
        return t        # t부터 출력해야 1이 가장 먼저 출력된다
  
my_counter = OddCounter()
print(next(my_counter))
print(my_counter.__next__())
print(my_counter.__next__())
print(my_counter.__next__())
