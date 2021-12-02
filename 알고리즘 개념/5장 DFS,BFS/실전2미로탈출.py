from collections import deque

n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input()))) #판 받기 

#상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(x,y):

    #큐 구현을 위해 deque 함수사용
    queue = deque()
    queue.append((x,y))

    #큐가 빌때까지반복
    while queue:
        print(queue)
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위 초과시
            if nx <= -1 or nx >= n or ny <= -1 or ny >=m:
                continue

            #벽인경우 무시
            if graph[nx][ny] == 0:
                continue

            #해당 노드를 처음으로 찍고 갔을때 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

#그래프의 탈출구 위치까지 최단거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))
    