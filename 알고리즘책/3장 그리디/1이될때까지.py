import time
n,k = map(int,input().split())

start = time.time()
count = 0
while True:
    if int(n) == 1: #n이 1이되면 조건문종료
        break

    if n % k == 0: # n이 k로 나눠지는 수일때 ->조건1
        n = n // k # n은 k로 나눠진 몫
        count += 1 # 카운트 1추가
    else: # n이 k로 나눠지지않을때 ->조건2
        n = n - 1 #n에서 1 빼주기
        count += 1 #카운트 1추가

print(count)
print("걸린시간 : ",time.time()-start)


