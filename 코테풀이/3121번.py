def solution(money, costs):

    answer = 0
    cost= [1,5,10,50,100,500]
    temp = []
    lst = []

    for i in range(len(costs)):
        temp.append(cost[i] / costs[i])
    for i in range(len(costs)):
        lst.append([temp[i],cost[i],costs[i]])
    lst.sort(reverse=True)
    print(lst)
    imsi = []
    for i in range(len(lst)):
        a = money //lst[i][1]
        money = money % lst[i][1]
        imsi.append(a)
    print(imsi)

    answerlst = []
    for i in range(len(lst)):
        answerlst.append(lst[i][2] * imsi[i])
    
    answer = sum(answerlst)
    print(answer)
    return answer

solution(4578,	[1, 4, 99, 35, 50, 1000])

solution(1999,[2, 11, 20, 100, 200, 600])