def solution(left, right):
    answer = 0
    temp = []
    for i in range(left,right+1):
        count = 0

        for j in range(1,i+1):
            if i % j == 0:
                count += 1
        temp.append([i,count])

    print(temp)
    
    for i in range(len(temp)):
        if temp[i][1] % 2 == 0: #짝수이면
            answer += temp[i][0]
        else:
            answer -= temp[i][0]

    print(answer)
    return answer


left = 13
right = 17

solution(left,right)