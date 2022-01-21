import sys
input = sys.stdin.readline
N = int(input())
max_value = 0

dp= [0] * (N+1)
t = []
p = []

for _ in range(N):
    day, cost = map(int,input().split())
    t.append(day)
    p.append(cost)

for i in range(N-1,-1,-1):
    time = t[i] + i
    #상담이 기간안에 끝나는경우
    if time <= N:
        dp[i] = max(p[i] + dp[time], max_value)
        print(dp)
        max_value = dp[i]

    #상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value


print(max_value)

# 입력예제
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200