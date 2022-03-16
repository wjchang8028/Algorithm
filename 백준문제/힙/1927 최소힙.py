import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
heapq.heapify(heap)

for i in range(n):
    x = int(input())

    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0:
        print(heapq.heappop(heap))
    elif x != 0:
        heapq.heappush(heap,x)

    print(heap)
