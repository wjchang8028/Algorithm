INF = int(1e9)

n,m = map(int,input().split()) #n = 노드 m = 간선

graph = [[INF] * (n+1) for _ in range(n+1)] #2차원그래프 생성

for i in range(1,n+1): #플로이드워셜그래프에서 0,0 라인 대각선은 0으로 초기화
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m): #a 에서 b거리가 1임(+양방향)
    a,b = map(int,input().split())

    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int,input().split()) #최종 도착지, 회사 방문지

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) #점화식 Dab = min(Dab, Dak + Dkb)

distance = graph[1][k] + graph[k][x] 

if distance >= INF:
    print(-1)
else:
    print(distance)


# 예제입력
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

#1 -> 3 -> 5-> 4 이동 (총거리 3)