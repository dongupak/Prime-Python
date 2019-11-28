
# 코드 4-30 : 재귀함수를 이용하여 정의한 피보나치 수열


def fibonacci(n):   # 피보나치 함수의 재귀적 구현
   if n <= 1:       # 피보나치 함수의 종료조건
       return n  
   else:  
       return(fibonacci(n-1) + fibonacci(n-2))  # F_n = F_(n-1) + F_(n-2)

nterms = int(input("몇 개의 피보나치수를 원하세요? "))  

# 음수일 경우 피보나치 수를 구할 수 없음.
if nterms <= 0:  
   print("오류 : 양수를 입력하세요.")  
else:  
   print("Fibonacci 수열: ", end = '')  
   for i in range(nterms):  
       print(fibonacci(i), end=' ') 
