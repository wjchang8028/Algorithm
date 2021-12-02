primes=[] # 소수를 담을 리스트
list = []
while True:
    n = int(input())    
    end = 2 * n
    if n == 0:
        break

    a = [False,False]+[True]*(end-1) # a리스트에서 0,1은 소수가 아니므로 제외 . 나머지는 true로 배열생성


    for i in range(2,int(end**0.5 + 1)): #2부터 소수판별
        if a[i]: 
            primes.append(i) # 2부터 n+1까지 리스트에 삽입
            for j in range(2*i, end + 1 , i): #i의 배수 다음항부터 (i = 2일때 4부터) n+1까지 i씩(배수)증가
                a[j] = False #소수가 아닌부분은 False로 변경
    
    for i in primes:
        if i > n:
            list.append(i)
    print(len(list))
    primes.clear()
    list.clear()