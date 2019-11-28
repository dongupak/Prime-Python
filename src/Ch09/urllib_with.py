
# 코드 9-25 : with 문을 사용한 웹 접속


import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()
    print(html)
