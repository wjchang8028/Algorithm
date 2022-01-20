import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split()) # 노드 간선 후보지
    start,g,h = map(int,input().split()) #시작지점 g h사이 도로 지나감 우회 x

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        # a->b가 c비용
        graph[a].append((b, c))
        graph[b].append((a, c))

    hubo = []
    for _ in range(k):
        hubo.append(int(input()))


    first = dijkstra(start)
    g_dijk = dijkstra(g)
    h_dijk = dijkstra(h)

    arr = []

    for b in hubo:
        if first[g] + g_dijk[h] + h_dijk[b] == first[b] or first[h] + h_dijk[g] + g_dijk[b] == first[b]:
            arr.append(b)

    arr.sort()
    # print(arr)

    for i in arr:
        print(i,end=" ")
    print()
    
