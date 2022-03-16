import heapq

def my_solution(scoville, K):
    answer = 1
    scoville.sort()
    while len(scoville) > 2:
        min_scov = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville,min_scov)

        if min(scoville) < K:
            answer += 1
        elif max(scoville) < K:
            answer = -1

        print(scoville,answer)

    print(answer)
    return answer

def solution(scoville,K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        min_value = heapq.heappop(scoville)

        if min_value >= K:
            break
        if len(scoville) == 0:
            return -1

        sec_min_value = heapq.heappop(scoville)
        mix_value = min_value + sec_min_value * 2
        heapq.heappush(scoville,mix_value)
        answer += 1

    return answer

solution([1, 2, 3, 9, 10, 12],	7)

