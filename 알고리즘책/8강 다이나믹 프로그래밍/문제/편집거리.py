# 두 문자가 같은 경우 : dp[i][j] = dp[i-1][j-1]
# 두 문자가 다른 경우 : dp[i][j] = 1 + min(dp[i][j-1] , dp[i-1][j] , dp[i-1][j-1]) # 삽입, 삭제 , 교체 순

A = input()
B = input()

def edit_dist(str1,str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dp[i][0] = i
    for j in range(1,m+1):
        dp[0][j] = j

    for i in range(1,n+1):
        for j in range(1,m+1):
            #문자가 같으면 왼쪽위 수를 그대로 대입
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            
            #문자가 다르다면 3가지 경우 최솟값
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) #삽입(왼쪽) , 삭제(위쪽) , 교체(왼쪽위) 중에서 최소비용 찾아 대입
    print(dp)
    return dp[n][m]

print(edit_dist(A,B))