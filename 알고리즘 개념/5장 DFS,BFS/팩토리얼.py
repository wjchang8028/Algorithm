def interactive_factorial(n):
    result = 1 #초기값
    
    for i in range(1,n+1):
        result *= i
    return result

print("반복적 재귀문장 : " , interactive_factorial(10))

def reculsive_factorial(n):
    result = 1

    if n <= 1: #값이 0이나 1이 들어왔을때 
        return 1    
    return n * reculsive_factorial(n-1)

print("재귀적 문장 : " , reculsive_factorial(10))