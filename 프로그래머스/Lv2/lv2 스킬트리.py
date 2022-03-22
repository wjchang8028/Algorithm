def solution(skill, skill_trees):
    answer = 0
  
    skill_list = list(skill)
    print(skill_list)

    for i in skill_trees:
        imsi = []
        for j in skill_list:
            if j in i: # 스킬이 스킬트리에 있다면
                temp = i.index(j)
                imsi.append(temp)
                
            else:
                imsi.append(-1)
        print(i,imsi)

        for k in range(1,len(imsi)):
            if imsi[k] > imsi[k-1]:
                pass


    print(answer)
    return answer


solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"])