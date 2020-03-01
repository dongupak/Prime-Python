# 코드 5-8 : 리스트 요소들을 하나하나 꺼내서 출력하기
## "으뜸 파이썬", p. 299

list1 = [10, 20, 30, 40, 50]
i = 0
for n in list1:
    list1[i] = n * 10
    i = i + 1

print(list1)
