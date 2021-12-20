def solution(d, budget):
    answer = 0
    temp = []
    d.sort()

    for i in d:
        answer += i
        if answer <= budget:
            temp.append(i)

    print(temp)
    answer = len(temp)
    
    return answer

d = [2,2,3,3]
# d = [1,3,2,5,4]
budget = 10
solution(d,budget)