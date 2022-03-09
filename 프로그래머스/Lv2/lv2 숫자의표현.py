def solution(n):
    answer = 0
    for i in range(1,140):
        if n < 1 + sum(range(i)):
            break

        if (n-sum(range(i))) / i == int((n-sum(range(i)))/i):
            answer += 1
    
    print(answer)
        
    return answer

def other_solution(n):
    answer = 0

    for i in range(1,n+1):
        total = 0
        for j in range(i,n+1):
            total += j

            if total > n:
                break
            elif total == n:
                answer += 1
    
    print(answer)

    return answer

solution(15)
other_solution(15)