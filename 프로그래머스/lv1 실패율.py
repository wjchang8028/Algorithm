def solution(N, stages):
    answer = []
    temp = []

    for i in range(1,N+1):
        
        a = stages.count(i)
        count = 0
        for j in stages:
            if j >= i:
                count += 1
        
        print(count)
            
        answer.append([a / count,i])
        answer.sort(key= lambda x: (x[0], -x[1]),reverse=True)

    print(answer)
    
    for i in range(len(answer)):
        temp.append(answer[i][1])
    
    print(temp)

    return temp


def correct(n,stages):
    result = {}
    denominator = len(stages)

    for stage in range(1,n+1):
        if denominator != 0:
            count =stages.count(stage)
            result[stage] = count / denominator
            denominator -= count

        else:
            result[stage] = 0

    answer = sorted(result, key= lambda x: result[x],reverse=True)

    print(answer)
    return answer

n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

correct(n,stages)