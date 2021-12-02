import sys
sys.setrecursionlimit(10**6)
testcase = int(input())

def dfs(x,y): #좌표

    if x<0 or x >=n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0 #간곳은 0으로 변경
        
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

        return True
    return False

for i in range(testcase):
            

    n,m,case = map(int,sys.stdin.readline().split())
    graph = [[0] * (m+1) for _ in range(n+1)] #밭 생성

    for i in range(case):
        x,y = map(int,sys.stdin.readline().split())
        graph[x][y] = 1 #배추위치 넣기

    # print(graph)

    result = 0

    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1

    print(result)


    


