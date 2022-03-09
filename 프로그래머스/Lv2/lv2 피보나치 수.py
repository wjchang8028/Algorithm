
def solution(n):
    answer = 0
    fibo = [0,1,1]
    for i in range(3,n+1):
        fibo.append((fibo[i-2]+fibo[i-1]) % 1234567 )
    answer = fibo[n]
    return answer

solution(3)
solution(1000)