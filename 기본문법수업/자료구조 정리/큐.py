                # 큐
                # 가장 먼저 삽입된 데이터


                # 우선순위 큐  (힙사용.)
                # 가장 우선순위가 높은 데이터
                # 최소힙 (가장 값이 낮은 데이터) 최대힙 (가장 값이 높은 데이터부터)
import heapq

def minheapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h,value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

def maxheapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h,-value)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = minheapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
result = maxheapsort([1,3,5,7,9,2,4,6,8,0])
print(result)