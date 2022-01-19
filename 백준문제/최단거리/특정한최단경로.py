import heapq
import sys

def solution(start,end):
    distance = [INF] * (n+1) #거리 저장
    distance[start] = 0 #시작 노드. 0으로 초기화
    q = [[0,start]] 

    while q:
        print(q)
        k,u = heapq.heappop(q)

        if k > distance[u]: # 노드의 거리보다 k가 크면 생략
            continue

        for w,v, in graph[u]: # 
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                heapq.heappush(q,[distance[v],v])
    return distance[end]


n,m = map(int,sys.stdin.readline().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append([w,v])
    graph[v].append([w,u])

stop1, stop2 = map(int,sys.stdin.readline().split())

#1 -> stop1 -> stop2 -> N
path1 = solution(1,stop1) + solution(stop1,stop2) + solution(stop2,n)

#1 -> stop2 -> stop1 -> N
path2 = solution(1,stop2) + solution(stop2,stop1) + solution(stop1,n)

if path1 >= INF and path2 >=INF:
    print(-1)
else:
    print(min(path1,path2))