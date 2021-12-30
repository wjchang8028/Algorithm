def solution(priorities, location):
    answer = 0
    
    queue = [(i,p)for i,p in enumerate(priorities)] #키값 붙여주기
    print(queue)

    while True:
        left = queue.pop(0)

        if any(left[1] < q[1] for q in queue): #맨왼쪽값이  가장 큰수가 아닐경우
            queue.append(left)

        else:   #맨왼쪽값이 가장 큰수일경우
            answer += 1
            if left[0] == location:
                print(answer)
                return answer


solution([2,1,3,2],2)