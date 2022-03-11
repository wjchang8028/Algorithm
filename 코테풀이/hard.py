def solution(N, L):
    answer = 0
    xlist = []
    ylist = []
    for i in range(len(L)):
        for j in range(len(L[i])):
            if j % 2 == 0:
                xlist.append(L[i][j])
            else:
                ylist.append(L[i][j])
    xlist.sort()
    ylist.sort()

    for i in range(1,len(xlist)):
        if xlist[i-1] == xlist[i]:
            answer += 1
            xlist[i-1] = xlist[i-1] - 1
    print(answer)

    return answer

solution(3,[[5,7,6,6],[3,9,5,4],[8,2,7,6]])