

def solution(s):
    answer = 0
    arr = list(map(int,s))
    print(arr)

    if arr[0] == 0:
        answer = arr[0] + arr[1] 
        for i in range(2,len(arr)):
            answer *= arr[i]
    else:
        answer = 1
        for i in range(len(arr)):
            answer *= arr[i]

    print(answer)
    return answer

def correct_solution(s):
    answer = 0
    arr = list(map(int,s))

    answer = arr[0]

    for i in range(1,len(arr)):
        num = arr[i]

        if num <= 1 or answer <= 1: #둘중 하나라도 0이거나 1인 경우 (1,1,1,1) 일때. 더해주는게 더 커짐
            answer += arr[i]
        else: #둘다 1보다 큰경우
            answer *= arr[i]

    print(answer)
    return answer
s = '1111115'
solution(s)
correct_solution(s)