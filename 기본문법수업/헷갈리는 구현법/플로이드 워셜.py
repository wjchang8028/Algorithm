# 노드의 갯수가 적을때 사용하는 최단거리 알고리즘
# O(n3) 약 500개까지 사용가능

# 점화식
# Dab = min(Dab,Dak + Dkb)

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("도달 불가",end=" ")
        else:
            print(graph[a][b],end=" ")
    print()
