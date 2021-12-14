def solution(answers):
    temp = []

    supoja1 = [1,2,3,4,5]
    supoja2 = [2,1,2,3,2,4,2,5]
    supoja3 = [3,3,1,1,2,2,4,4,5,5]

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for i in range(len(answers)):
        if answers[i] == supoja1[i%5]:
            cnt1 += 1
        if answers[i] == supoja2[i%8]:
            cnt2 += 1
        if answers[i] == supoja3[i%10]:
            cnt3 += 1
    if max(cnt1,cnt2,cnt3) == cnt1:
        temp.append(1)
    if max(cnt1,cnt2,cnt3) == cnt2:
        temp.append(2)
    if max(cnt1,cnt2,cnt3) == cnt3:
        temp.append(3)
    
    print(temp)
    answer = temp
    
    return answer

answer = [1,2,3,4,5]
# answer = [1,3,2,4,2]
solution(answer)