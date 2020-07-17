# 코드 9-8 : 인스턴스의 아이덴티티 연산자 : is, is not 연산자
## "으뜸 파이썬", p. 543

list_a = [10, 20, 30]     # 리스트 객체를 참조하는 list_a
list_b = [10, 20, 30]     # 리스트 객체를 참조하는 list_b
if list_a is list_b:      # 두 리스트 객체가 같은지 검사함
    print('list_a is list_b')
else:
    print('list_a is not list_b')
