def solution(name):
    answer = 0
    joystick = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") #26개
    namelist = list(name)
    move = []
    temp = []

    for i in namelist:
        count = 0
        for j in joystick:
            count += 1
            if i == j:
                move.append(count - 1)
                break 

    for i in move:
        if 26 - i  < i:
            temp.append(i-26)
        else:
            temp.append(i)
    print(temp)

    for i in range(len(temp)):
        if temp[i] < 0:
            temp[i] = temp[i] * -1
    print(temp)

    answer = sum(temp)


    for i in temp:
        if i == 0:
            if temp.index(i) <= len(temp) // 2:
                answer += len(temp) - (temp.index(i) + 1 )
        else:
            answer += 1

    answer -= 2
    print(answer)
    return answer


name = "JAN"
solution(name)

#JAZ 최소 11번 j로 9번, 왼쪽눌러서 z로 이동후 뒤로 1칸 = 9 , 0 , 1 총 11번
#JAN 최소 23번
#JEROEN 최소 56번

#조건 : 기존값 AAA가 주어질때 조이스틱을 최소로 돌려서 만들기