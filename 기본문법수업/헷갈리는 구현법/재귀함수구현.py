#팩토리얼 구현
def factorial(n):
    if n <= 1: # 0!,1! = 1
        return 1
    return n * factorial(n-1)

print(factorial(5))

#유클리드호제법(최대공약수)  = A,B와 A를 B로 나눈 나머지R 이 있을때,  A와 B의 최대공약수 = B와 R의 최대공약수
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b,a%b)

print(gcd(192,168))