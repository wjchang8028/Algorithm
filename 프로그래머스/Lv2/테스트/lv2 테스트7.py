from itertools import combinations, permutations, product


def solution(numbers):
    lst = []
    answer = 0
    temp = ''
    for i in range(1,len(numbers)+1):
        temp += list(''.join, permutations(numbers,i))
        
        print(temp)




    return answer

solution("17")
solution("011")