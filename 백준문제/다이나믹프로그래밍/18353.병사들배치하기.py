n = int(input())

array = list(map(int,input().split()))
array.reverse()
dp = [1 for i in range(n)]

for i in range(1,n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(dp)
print(n-max(dp))