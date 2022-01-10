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

print(result)

    
