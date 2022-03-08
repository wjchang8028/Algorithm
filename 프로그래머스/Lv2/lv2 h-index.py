def solution(citations):
    answer = 0
    
    for i in citations:
        cnt = 0
        for j in citations:
            if i <= j:
                cnt += 1

        if i >= cnt:
            answer += 1
                 
        
    
    print(answer)
    return answer

solution([3, 0, 6, 1, 5])
solution([10, 10, 10, 10, 10])