# 5 8 3
# 2 4 5 4 6

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

#가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k  # [ 6 6 6 5 ]가 반복이므로 2 * 3 해서 총 6개 나옴
count += m % (k+1) # 갯수가 나눠 떨어지지않을때 가장 큰수가 추가로 더해져야함

result = 0
result += (count) * first
result += (m-count) * second
print(result)

