
# 코드 12-29 : 제너레이터의 예제


def create_gen():
    alist = range(1, 4)
    for x in alist:
        yield x

my_generator = create_gen()
print(my_generator)
for n in my_generator:
    print(n)
