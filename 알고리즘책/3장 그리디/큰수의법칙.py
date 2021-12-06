import sys
n , m ,k = map(int,input().split())


data = list(map(int,sys.stdin.readline().split()))

data.sort()

print(data)

#가장큰수
print(data[n-1])
#두번째 큰수
print(data[n-2])

first = data[n-1]
second = data[n-2]

result = 0


while True:
    for i in range(k): #k값 만큼 더해주기
        if m == 0: # m번 반복되면 for문종료
            break

        result += first #첫번째값을 result에 더하기
        m -= 1 # 한번더할때마다 m이 1씩줄음
    if m == 0: # m 이 0이 되면 종료
        break

    result += second
    m -= 1

print(result)