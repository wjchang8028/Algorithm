from itertools import chain, permutations

def solution(numbers):
    answer = 0
    primes=[]
    temp = []
    numArr = []

    array = list(numbers) #각 번호
    # print(array)
    
    temp = list(set(chain.from_iterable(permutations(array,r) for r in range(1,len(array)+1)))) # 각 번호로 조합할 수 있는 모든 경우의 수
    # print(temp)

    for i in range(len(temp)):
        numArr.append(''.join(temp[i]))
    numArr = list(set(map(int,numArr)))
    numArr.sort()
    print(numArr) #int형으로 변환한 모든 숫자조합

    print(max(numArr))

    a = [False, False]+[True] * (max(numArr)+1)
    for i in range(2,max(numArr)+2):
        if a[i]:
            primes.append(i)
            for j in range(2*i,max(numArr)+2,i):
                a[j] = False
    
    print(primes)

    for i in numArr:
        if i in primes:
            answer += 1
    print(answer)

    return answer

def other_solution(numbers):
    a = set()

    for i in range(len(numbers)):
        a |= set(map(int,map("".join,permutations(list(numbers), i+1 )))) #|= or연산자를 하고 난 값으로 새로이 update한다는 의미
    print(a)

    a -= set(range(0,2)) # 0과 1은 소수판별에 필요하지 않으므로 삭제
    print(a)
    
    for i in range(2,int(max(a)**0.5) + 1): #에라토스테네스 체
        a -= set(range(i*2,max(a),i)) # 조합에서 소수가 아닌 수들을 제거

    print(a)
    return len(a)

# solution("1300")
other_solution("011")