
# 코드 5-10 : 리스트 요소들을 하나하나 방문하며 10을 곱하는 기능


list1 = [10, 20, 30, 40, 50]
i = 0
for n in list1:
    list1[i] = n * 10
    i = i + 1
    
print(list1)
