# 코드 11-1 : 선형 연립 방정식 풀이
## "으뜸 파이썬", p. 664

import numpy as np

a = np.array([[2, 3], [1, -2]])
b = np.array([1, 4])
x = np.linalg.solve(a, b)

print(x)
