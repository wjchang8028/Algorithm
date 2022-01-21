import sys
input = sys.stdin.readline

n = int(input())
dp = [] # DP테이블 초기화

for _ in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n): # 둘째 줄 부터 돌리고
    for j in range(i+1): # 삼각형 열의 길이는 행 + 1
        # 왼쪽위에서 내려오는 경우
        if j == 0: # 범위 밖
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        
        #위에서 내려오는경우
        if j == i: #범위 밖 ex) 5
                              # 7 3  3위에는 아무것도 없기때문
            up = 0
        else:
            up = dp[i-1][j]

        #최대합을 저장
        dp[i][j] = dp[i][j] + max(up_left,up)
print(dp)
print(max(dp[n-1])) # 해당 줄의 가장 큰값 출력

# 입력예제

# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5