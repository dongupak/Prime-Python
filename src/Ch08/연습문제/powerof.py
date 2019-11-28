import math

def print_pow():
    t = 2
    for n in range(2, 11):
        print('{}의{:3d}제곱 = {:4.0f}'.format(t, n, math.pow(t, n)))
