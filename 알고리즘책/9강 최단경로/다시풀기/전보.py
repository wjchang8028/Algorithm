import sys
import heapq

n,m,start = map(int,sys.stdin.readline().split())

INF = int(1e9)
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) 
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

print(graph)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

city = 0
total_time = 0
for i in distance:

    if i == INF:
        pass
    else:
        city += 1
        total_time = max(total_time,i)
print(city - 1)
print(total_time)

# 4 4 1
# 1 2 4
# 1 3 2
# 2 3 5
# 3 4 8

# 3 , 10