#공포 수치대로 그룹짜서 최대한 많이. 
#많이 무서운사람은 놔두고 가도됨

def solution(n , horror_list):
    answer = 0

    horror_list.sort()
    print(horror_list)

    while horror_list:
        max_group = horror_list.pop(0)
        if len(horror_list) <= max_group:
            break

        del(horror_list[0:max_group-1])
        answer += 1
        
        
    print(answer)
    return answer

def correct_solution(n,horror_list):
    horror_list.sort()
    answer = 0
    count = 0

    for i in horror_list:
        count += 1 #그룹내 인원수
        if count >= i: #공포가 인원수와 같거나 많아지면 
            answer += 1 # 그룹하나 출발
            count = 0 #다시 처음부터 인원수세기

    print(answer)
    return answer



n = 4
horror_list = [20,10,9,8,3,4,1,1,3,2,1,3,3,4,1,1,3,2,1,3,3,5,6,1,1,3,2,1,3,3,4,1,1,3,2,1,3,3,4,1,1,3,2,1,3,3,4,1,1,3,2,1,3]
# horror_list = [21,1,1,1]
solution(n,horror_list)

horror_list = [20,10,9,8,3,4,1,1,3,2,1,3,3,4,1,1,3,2,1,3,3,5,6,1,1,3,2,1,3,3,4,1,1,3,2,1,3,3,4,1,1,3,2,1,3,3,4,1,1,3,2,1,3]
# horror_list = [21,1,1,1]
correct_solution(n,horror_list)