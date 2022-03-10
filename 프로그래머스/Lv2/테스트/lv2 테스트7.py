from itertools import combinations, permutations, product
def IsPrime(num):
    if num == 0 or num == 1:
        return False

    for i in range(2,num): 
        if num % i == 0:
            return False
    return True

def solution(numbers):
    lst = []
    answer = 0
    temp = ''
    a = set() 
    for i in range(len(numbers)):
        a |= set(map(int,map("".join,permutations(list(numbers), i+1 )))) #|= or연산자를 하고 난 값으로 새로이 update한다는 의미
    arr = list(a)
    arr.sort()
    print(arr)

    cnt = 0
    for i in arr:
        if IsPrime(i):
            cnt += 1
        else:
            pass
    
    print(cnt)

    return answer

solution("17")
solution("011")