from collections import deque

def solution(prices):
    answer = []
    
    while prices:
        cursor = prices.pop(0)

        count = 0
        for i in range(len(prices)):
            count += 1
            if prices[i] < cursor: #값이 커서보다 떨어지면
                break
        answer.append(count)

    print(answer)

    return answer

def solution2(prices):
    answer =[]
    q = deque(prices)

    while q:
        cursor = q.popleft()
        count = 0

        for i in range(len(q)):
            count += 1
            if q[i] < cursor:
                break
        answer.append(count)

    print(answer)
    return answer

solution2([1, 2, 3, 2, 3])