
def firstsolution(logs):
    answer = 0
    lst = ['team_name','application_name','error_level','message']

    for i in logs:
        if len(i) > 100:
            answer += 1
        else:
            arr = list(i.split(" "))
            # print(arr)
            for j in range(len(arr)):
                if arr[j] not in lst:
                    answer += 1
                    break
                    
    print(answer-1)

    return answer

# solution(["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"])

# solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"])

def secondsolution(sentences, n):
    answer = 0
    arr = []
    temp = []
    for i in sentences:
        temp.append(list(set(i)))
    print(temp)

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j].islower() != temp[i][j]:
                arr.append('shift')
                arr.append(temp[i][j])
            elif temp[i][j].islower() == temp[i][j]:
                arr.append(temp[i][j])

            print(arr)
    print(answer)
    return answer

secondsolution(["line in line", "LINE", "in lion"],5)
secondsolution(["ABcD", "bdbc", "a", "Line neWs"],7)


def thirdsolution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    temp = []
    homework = []
    print(remote_tasks) # 재택
    print(office_tasks) # 출근

    for i in employees:
        temp.append(list(i.split(" ")))
    
    print(temp)


    for i in range(len(temp)):
        temp[i].append(i+1)
        for j in range(len(temp[i])):
            if temp[i][j] in remote_tasks:
                pass
            elif temp[i][j] in office_tasks:
                temp[i][0] = 0
                break

    print(temp)

    imsi = []


    for i in temp:
        if i[0] != 0 :
            answer.append(i[-1])

    print(answer)

    
    return answer

def thirdsolution_2(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    temp = []
    for i in employees:
        imsi = 1
        temp.append(list(i.split(" ")))

    for i in range(len(temp)):
        temp[i].append(i+1)
        for j in range(len(temp[i])):
            if temp[i][j] in remote_tasks:
                pass
            elif temp[i][j] in office_tasks:
                temp[i][0] = 0
                break

    # print(temp)

    dic = {}

    for key in temp:
        dic.setdefault(int(key[0]),[]).append(key[0:])

    print(dic)

    for i in range(1, num_teams + 1):
        for j in range(len(dic[i])):
            if dic[i][j] not in office_tasks:
                answer.append(dic[i][j][-1])


    print(answer)
    return answer
# thirdsolution_2(3,["development","marketing","hometask"],	["recruitment","education","officetask"],["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"])

def fourthsolution(arr, brr):
    answer = 0
    for i in range(1,len(arr)):
        
        temp = arr[i-1] - brr[i-1]

        if temp > 0:
            arr[i-1] -= temp
            arr[i] += temp
            answer += 1
        elif temp < 0:
            arr[i-1] -= temp
            arr[i] += temp
            answer += 1
        
        print(arr,temp)

    
    # print(answer)
    return answer

# solution([3, 7, 2, 4],[4, 5, 5, 2])
# solution([6, 2, 2, 6],[4, 4, 4, 4])

def fifthsolution(abilities, k):
    answer = 0
    abilities.sort(reverse=True)
    print(abilities)

    me = 0 
    enemy = 0

    while abilities:
        player = abilities.pop(0)
        
    
    print(me, enemy)



    return answer

# solution([2, 8, 3, 6, 1, 9, 1, 9], 2)
# solution([7, 6, 8, 9, 10], 1)

def sixthsolution(req_id, req_info):
    answer = []
    return answer

# solution(["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"],[[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]])
