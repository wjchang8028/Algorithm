# 출발노드 설정
# 최단거리 테이블 초기화
# 방문하지 않은 노드중 최단거리가 가장 짧은 노드 선택
# 해당 노드를 거쳐 다른 노드로 가는 비용 계산하여 최단거리 테이블 갱신
# 3번 4번 반복

# 시간 복잡도 O(v2) => 노드의 갯수가 5000개 이하라면 가능. 
 
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("도달할 수 없음")
    else:
        print(distance[i])

# 힙을 사용한 개선된 다익스트라 O(ElogV) 노드가 5000개 이상일 경우 사용
import heapq
def heapdijkstra(start):
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

heapdijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("갈 수 없는 곳입니다")
    else:
        print(distance[i])

