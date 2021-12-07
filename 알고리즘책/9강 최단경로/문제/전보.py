import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n,m,start = map(int,input().split()) #도시갯수,통로갯수,메세지보내는 도시

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int,input().split())

    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))

    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

count = 0
max_distance = 0

for i in distance:
    if i != INF:
        count += 1
        max_distance = max(max_distance,i)

print(count - 1, max_distance)

# 입력예제

# 3 2 1
# 1 2 4
# 1 3 2

# 결과 : 2 4

