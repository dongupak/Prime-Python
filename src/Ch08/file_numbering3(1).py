# 코드 8-23 : try-except 문을 사용한 파일 입출력
## "으뜸 파이썬", p. 507

import sys

success = True
fname = input('입력 파일명: ')
try:
  f = open(fname, 'r', encoding = 'UTF8') # 파일 열기
except IOError:
  print('Could not read file:', fname)
  success = False
except:
  print('Unexpected error: ', sys.exc_info()[0])
  success = False

if success:
  n = 1
  l = f.readline()
  while l:
    print('{:3d}: {}'.format(n, l), end = '')
    n += 1
    l = f.readline()
  f.close()    # open() 함수와 너무 멀리 떨어져있음

print('file access successful? ', success)
