import heapq
import sys
input = sys.stdin.readline

max_heap = []
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if len(max_heap) == 0:
            print(0)
        else:
            print((-1) * heapq.heappop(max_heap))
            
    if x != 0:
        heapq.heappush(max_heap,-1 * x)
    
# 최대힙은 최소힙 구현에서 -1 만 곱해주면 됨
        
# 13
# 0
# 1
# 2
# 0
# 0
# 3
# 2
# 1
# 0
# 0
# 0
# 0
# 0