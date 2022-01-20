import sys
input = sys.stdin.readline

n = int(input()) # 도시 수(노드)
m = int(input()) # 버스 수(간선)
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b,c = map(int,input().split()) # a : 시작도시 b:도착도시 c:비용
    graph[a][b] = min(graph[a][b],c) # 겹치는 구간은 더 작은 비용의 버스를 이용할 것


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
# print(graph)

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] >= INF:
            graph[a][b] = 0
            print(graph[a][b],end=" ")
        else:
            print(graph[a][b],end=" ")
    print()



