# 코드 5-10 : 리스트 요소들을 하나하나 방문하며 10을 곱하는 기능
## "으뜸 파이썬", p 300 - 참고 코드

list1 = [10, 20, 30, 40, 50]
i = 0
list2 = []
for n in list1:
    list2.append( n * 10 )
    
print(list2)
