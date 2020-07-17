# 코드 9-10 : 두 개의 문자열 참조변수와 is, is not 연산
## "으뜸 파이썬", p. 545

a = 'ABC'           # 문자열 객체를 참조하는 변수 a
b = 'ABC'           # 문자열 객체를 참조하는 변수 b
if a is b:          # 문자열 객체 a, b가 같은가 비교
    print('a is b') # 문자열 객체 a, b는 같은 객체를 참조함
else:
    print('a is not b')
