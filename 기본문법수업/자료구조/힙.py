import heapq

#최초 힙 생성
heap = []

#힙에 원소 추가
heapq.heappush(heap,4) #원소를 추가할 리스트 , 추가할 원소
heapq.heappush(heap,1)
heapq.heappush(heap,3)
heapq.heappush(heap,5)
heapq.heappush(heap,4)

print(heap) #[1,4,3,5,4]

#힙 삭제 (가장 작은 원소를 삭제)
print(heapq.heappop(heap))
print(heap)

#힙의 최솟값(삭제하지않고) 두번째 세번째 인자들도 정렬되어있다는 보장은 없음
print(heap[0])

#기존 리스트를 힙으로 변환(마찬가지로 제일 작은 값은 0번째 인덱스에 들어가지만 뒤에는 정렬이 되어있지 않음)
p = [4,1,7,3,8,5]
heapq.heapify(p)
print(p)

#기본적으로 힙은 최소힙을 동작 -> 최대값은 활용해야함
nums = [4,1,7,3,8,5]
maxheap =[]

for num in nums:
    heapq.heappush(maxheap,(-num,num)) #우선순위 , 값

while maxheap:
    print(heapq.heappop(maxheap)[1])