# 생능 출판사 "으뜸 파이썬" 소스코드 저장소
## 이 책의 소스코드를 보실 수 있는 저장소 입니다.

- 소스코드는 다음과 같이 코드 x-x : 코드설명, 페이지 순서로 되어 있습니다.
- 혹시 책의 내용과 차이가 나는 부분이 있으면 저자 이메일로 알려주시거나 fork -> pull request로 알려주십시오.
- 오류 신고 : dongupak@gmail.com
<pre>
# 코드 4-6 : 매개변수를 사용하여 지정된 문자를 인자 값만큼 반복 출력하기
## "으뜸 파이썬", p. 205

def print_hello(n):             # 매개변수를 이용한 반복 출력
    print('Hello ' * n)


print('Hello를 두 번 출력합니다.')
print_hello(2)
print('Hello를 세 번 출력합니다.')
print_hello(3)
print('Hello를 네 번 출력합니다.')
print_hello(4)
<pre>
