def solution(n):
    answer = 0
    temp = []
    sosu = [False,False]+[True] * (n-1)

    for i in range(2,n+1):
        if sosu[i]:
            temp.append(i)
            for j in range(2*i,n+1,i):
                sosu[j] = False
    answer = sosu.count(True)
    return answer

solution(5)