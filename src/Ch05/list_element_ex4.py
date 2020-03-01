# 코드 5장 : 리스트 요소들을 하나하나 방문하며 10을 곱하는 기능
## "으뜸 파이썬", p. 300 - 참고 코드

list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)):   # len(list1)을 통해 모든 원소를 참조
     list1[i] = list1[i] * 10 # index i를 이용하여 갱신
    
print(list1)
