from collections import Counter

def solution(progresses, speeds):
    answer = []
    days = [] 
    stk = []

    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            days.append((100 - progresses[i]) // speeds[i])
        else:
            days.append((100 - progresses[i]) // speeds[i] + 1)
    days.reverse()  #걸리는 시간 스택 
    print(days)

    top = 0
    while days: # 시간리스트에서 구현완료 되는 시점으로 리스트 바꿔주기
        if days[-1] > top:
            top = days.pop()

        elif days[-1] <= top:
            days.pop()
            
        stk.append(top)

    print(stk)

    c = Counter(stk) #리스트에서 중복된 값의 수를 세주기
    answer = list(c.values())
    print(answer)

    return answer

solution([93, 30, 55],[1, 30, 5])
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])
solution([20, 99, 93, 30, 55, 10], [5, 10, 1, 1, 30, 5])