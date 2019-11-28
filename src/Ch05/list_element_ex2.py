
# 코드 5-9 : 리스트 요소들을 하나하나 방문하며 10을 곱하는 기능

list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)):
     list1[i] = list1[i] * 10
    
print(list1)
