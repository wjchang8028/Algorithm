#힙에 대한 라이브러리

import heapq # 파이썬 힙은 기본적으로 min heap 구조로 되어있음

arr = [11,1,3,2,5,6,9,4]

heapq.heapify(arr) # 리스트를 힙 형태로 만들어줌과 동시에 가장 작은값을 맨 앞으로 보내줌 (맨처음 sort해줄 시간 조차 줄이는 법)

while True:
    if len(arr) > 0: # arr의 길이가 1이 되면 탈출
        break

    print(arr)
    heapq.heappop(arr) # 가장 작은 값을 뽑아냄

arr2 = []
for i in range(10):
    heapq.heappush(arr2,i) # heappush(삽입배열,값)
print(arr2)