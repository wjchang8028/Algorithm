
def wrong_solution(id_list, report, k):
    answer = []
    result = []
    temp = []
    block = []
    ban_user=[]

    for i in range(len(report)):
        temp.append(report[i].split(" "))
    # print(temp)
    
    for i in range(len(id_list)):
        for j in range(len(temp)):
            if id_list[i] == temp[j][0]:
                block.append(temp[j][1])


    for i in range(len(id_list)):
        count = 0
        for j in range(len(block)):
            if id_list[i] == block[j]:
                count += 1
        if count == k:
            ban_user.append(id_list[i])
    # print(ban_user)

    for i in id_list:
        answer.append([i,0])
    # print(answer)

    for i in range(len(answer)):
        for j in range(len(temp)):
            if answer[i][0] == temp[j][0] and temp[j][1] in ban_user:
                answer[i][1] += 1
    
    # print(answer)

    for i in range(len(answer)):
        result.append(answer[i][1])
    
    print(result)
    return result

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list} # {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}
    print(reports)

    for r in set(report): # 동일 회원에 대한 신고는 1로 처리하므로 set
        reports[r.split()[1]] += 1
    
    print(reports) #신고당한 횟수
 
    for r in set(report):
        if reports[r.split()[1]] >= k: # 신고당한 횟수가 k보다 클때
            answer[id_list.index(r.split()[0])] += 1 # report의 신고한 유저부분을 인덱스로 갖는 곳에 +1 해주기
    
    print(answer)
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
solution(id_list, report,k)