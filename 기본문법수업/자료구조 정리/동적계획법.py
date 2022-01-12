# 메모이제이션은 탑다운방식 (하향식) O(N) 시간복잡도
# 한번 계산한 결과를 메모리공간에 메모하는 기법

                # 피보나치 (햐항식)
d = [0] * 100

def fibo(n):
    if n == 1 or n == 2:
        return 1
    
    if d[n] != 0:
        return d[n]
    
    d[n] = fibo(n-1) + fibo(n-2) 
    return d[n]
print(fibo(99))

                #상향식
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])
