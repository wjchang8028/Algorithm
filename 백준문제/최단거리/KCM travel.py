import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

def dijkstra(airport,clock,n,m):
    q = []
    heapq.heappush(q,(1,0,0))

    clock[1][0] = 0

    for cost in range(m+1):
        for here in range(1,n+1):
            if clock[here][cost] == INF:
                continue
    
            distance = clock[here][cost]
            for nextHere, nextCost, nextTime in airport[here]:
                if cost + nextCost > m:
                    continue

                clock[nextHere][cost + nextCost] = min(clock[nextHere][cost+nextCost],distance + nextTime)
    return clock

t = int(input())

for _ in range(t):
    n,m,k = map(int,input().split())

    airport = [[] for _ in range(n+1)]
    clock = [[INF for _ in range(m+1)] for _ in range(n+1)]

    for _ in range(k):
        src, dst, cost, time = map(int,input().split())
        airport[src].append((dst,cost,time))

    clock = dijkstra(airport,clock,n,m)
    if min(clock[n]) == INF:
        print("Poor KCM")
    else:
        print(min(clock[n]))