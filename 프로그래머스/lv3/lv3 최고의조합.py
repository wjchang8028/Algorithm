from itertools import combinations, permutations, product
from unittest import result


def solution(n, s):
    imsi = []
    answer = []
    temp = [i for i in range(s)]
    a = list(product(temp,repeat=n))

    for i in range(len(a)):
        if sum(a[i]) == s:
            imsi.append(a[i])
    
    # print(imsi)

    max_value = 1
    for i in range(len(imsi)//2 + 1):
        gop = 1
        for j in range(len(imsi[i])):
            gop *= imsi[i][j]
        max_value = max(max_value,gop)
    
    return answer

solution(2,9)
solution(2,8)

def other_solution(n,s):
    answer = []
    if n > s:
        return [-1]

    value = s // n

    for i in range(n):
        answer.append(value)
    
    print(answer)
    
    index = len(answer) - 1

    for i in range(s % n):
        answer[index] += 1
        index -= 1

    print(answer)
    return answer

other_solution(2,9)
other_solution(2,8)