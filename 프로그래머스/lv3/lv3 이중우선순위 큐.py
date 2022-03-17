import heapq
def solution(operations):
    answer = []
    arr = []
    heap = []
    max_heap=[]
    for i in operations:
        arr.append(list(i.split(' ')))
    print(arr)

    for i in arr:
        if i[0] == 'I':
            
            heapq.heappush(heap, int(i[1]))
            heapq.heappush(max_heap, (int(i[1]), (-1)* int(i[1])) )
        elif i[0] == 'D':
            if len(heap) != 0:
                if i[1] == '-1': # 최솟값 날리기
                    heapq.heappop(heap)
                else: # 최댓값 날리기
                    heapq.heappop(max_heap)
            else:
                pass
        print(heap)

    if len(heap) == 0:
        answer.append(0)
        answer.append(0)
    else:
        min_value = min(heap)
        max_value = max(heap)
        print(max_value,min_value)

    print(answer)

    return answer

solution(["I 16","D 1"])
solution(["I 7","I 5","I -5","D -1"])
solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])