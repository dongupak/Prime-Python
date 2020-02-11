# 코드 8-24 : try-except 문을 사용한 파일 입출력
## "으뜸 파이썬", p. 508

import sys

success = False
try:
  fname = input('입력 파일명: ')
  with open(fname, 'r', encoding = 'UTF8') as f:
    n = 1
    l = f.readline()
    while l:
      print('{:3d}: {}'.format(n, l), end = '')
      n += 1
      l = f.readline()
    success = True
except IOError:
  print('Could not read file:', fname)
except:
  print('Unexpected error:', sys.exc_info()[0])

print('file access successful? ', success)
