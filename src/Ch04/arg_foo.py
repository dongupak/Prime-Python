# 코드 4-27 : 가변 인자를 가지는 함수에서 len() 함수 활용
## "으뜸 파이썬", p. 232

def foo(*args):
    print('인자의 개수:', len(args))
    print('인자들 :', args)
    
foo(10, 20, 30)
