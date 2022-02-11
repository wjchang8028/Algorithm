def solution(arr):
    answer = []
    a = arr.pop(0)
    answer.append(a)

    for i in arr:
        if answer[-1] != i:
            answer.append(i)

    print(answer)
    return answer

arr = [1,1,1,3,3,0,1,1,1]
solution(arr)