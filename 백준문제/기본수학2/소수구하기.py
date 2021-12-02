m, n = map(int,input().split())


a = [False,False]+[True]*(n-1) # a리스트에서 0,1은 소수가 아니므로 제외 . 나머지는 true로 배열생성

primes=[] # 소수를 담을 리스트

for i in range(2,n+1): #2부터 소수판별
    if a[i] == True: 
        primes.append(i) # 2부터 n+1까지 리스트에 삽입
        for j in range(2*i, n+1 , i): #i의 배수 다음항부터 (i = 2일때 4부터) n+1까지 i씩(배수)증가
            a[j] = False #소수가 아닌부분은 False로 변경

for i in primes:
    if i >= m:
        print(i)