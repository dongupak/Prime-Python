# 코드 9-9 : 두 개의 리스트와 == 연산
## "으뜸 파이썬", p. 544

list_a = [10, 20, 30]     # 리스트 객체를 참조하는 list_a
list_b = [10, 20, 30]     # 리스트 객체를 참조하는 list_b
if list_a == list_b:      # 리스트 객체의 속성 값이 같은지 비교함
    print('list_a == list_b')
else:
    print('list_a != list_b')
