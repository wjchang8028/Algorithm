from collections import deque

m,n = map(int,input().split())

graph =[]
queue = deque([])

for i in range(n):
    graph.append(list(map(int,input().split())))

    for j in range(m): #익은 토마토들을 큐에 저장
        if graph[i][j] == 1:
            queue.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
   

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0: #범위 내, 그리고 안익은 토마토(0)일때
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1 #거리 증가

bfs()

result = 0

# print(graph)

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result,max(i))

print(result - 1) #처음시작을 1로했기때문에 마지막에 1다시 빼줌


