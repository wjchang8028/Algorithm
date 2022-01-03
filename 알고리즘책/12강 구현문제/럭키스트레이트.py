def solution(n):
    answer = ''
    left = []
    right = []

    lst = list(str(n))

    for i in range(len(lst)//2):
        left.append(int(lst[i]))
        
    for i in range(len(lst)-1, len(lst)//2 - 1 , -1):
        right.append(int(lst[i]))

    if sum(left) == sum(right):
        answer = 'LUCKY'
    else:
        answer = 'READY'

    print(answer)
    return answer



solution(123402)
solution(7755)