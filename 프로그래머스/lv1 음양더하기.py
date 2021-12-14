def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] *= -1
        else:
            pass
    answer = sum(absolutes)

    print(answer)
    return answer


absolutes = [4,7,12]
signs= [True,False,True]
solution(absolutes,signs)