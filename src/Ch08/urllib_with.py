# 코드 8-25 : with 문을 사용한 웹 접속
## "으뜸 파이썬", p. 509

import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()
    print(html)
