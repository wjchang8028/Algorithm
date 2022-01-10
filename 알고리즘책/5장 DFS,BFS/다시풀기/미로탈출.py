from collections import deque
n,m = 5, 6
# graph = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
graph = [[1,0,0,1,1,1],[1,0,0,0,1,1],[1,1,0,1,1,1],[0,1,1,1,0,1],[1,1,1,1,0,1]]

dx = [-1,1,0,0] #상 하 좌 우
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        # print(x,y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: #범위초과
                continue

            if graph[nx][ny] == 0: #벽을 만났을때.
                continue

            if graph[nx][ny] == 1: #길일때
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

                # print(queue)
    return graph[n-1][m-1]

n,m = 5, 6
graph = [[1,0,0,1,1,1],[1,0,0,0,1,1],[1,1,0,1,1,1],[0,1,1,1,0,1],[1,1,1,1,0,1]]

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] += 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        
    print(graph)
    print(graph[n-1][m-1])
    return graph[n-1][m-1]


print(bfs(0,0))
dfs(0,0)
