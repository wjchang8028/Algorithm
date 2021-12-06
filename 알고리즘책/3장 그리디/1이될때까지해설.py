import time


n,k = map(int,input().split())
start = time.time()

result = 0

while True:
    #n==k로 나누어져 떨어지는수가 될때까지 1씩빼기
    target = (n//k) * k
    result += (n - target)
    n = target

    #n이 k보다 작을때(더이상 나눌 수 없을때 )반복문 탈출
    if n<k:
        break
    # k로 나누기
    result += 1
    n //=k


#마지막으로 남은 수에 대하여 1씩빼기
result += (n-1)
print(result)
print("걸린시간 : ",time.time()-start)

