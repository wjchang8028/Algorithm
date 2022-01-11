n = 4
m = 5
pan = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]

def dfs(x,y):
    if x<= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if pan[x][y] == 0:
        pan[x][y] = 1
        dfs(x-1,y) #상
        dfs(x+1,y) #하
        dfs(x,y-1) #좌
        dfs(x,y+1) #우

        return True

    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

# print(result)

# =============================================================
from collections import deque

n = 4
m = 5
pan = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
dx = [-1, 1, 0, 0] #상하좌우
dy = [0 , 0,-1, 1]



def bfs(x,y):
    

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                return False

            if pan[nx][ny] == 1:
                return False

            if pan[nx][ny] == 0:
                pan[nx][ny] = 1

    print(pan)

bfs(0,0)
