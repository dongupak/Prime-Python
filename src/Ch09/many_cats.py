# 코드 9-3 : Cat 클래스 정의와 여러 개의 객체 생성
## "으뜸 파이썬", p. 532

class Cat:
    def meow(self):
        print('야옹 야옹~~~')

nabi = Cat()
nabi.meow()
nero = Cat()
nero.meow()
mimi = Cat()
mimi.meow()
