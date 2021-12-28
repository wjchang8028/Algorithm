def solution(brown, yellow):
    answer = []
    temp = []

    total = brown+yellow

    for garo in range(brown):
        for sero in range(brown):
            if garo * sero == total:
                temp.append([garo,sero])

    print(temp)

    for i in range(len(temp)):
        if temp[i][1] >= 3:
            if temp[i][0] >= temp[i][1]:
                if (temp[i][0] - 2) * (temp[i][1] - 2) == yellow:
                    answer = temp[i]

    print(answer)
    return answer

def other_solution(brown, red):
    for i in range(1, int(red**(1/2))+1): #가로 * 세로 = 격자 합, 둘레의 합(가로*2 + 세로*2 - 겹치는부분4) = 갈색 둘레
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]

solution(24,24)
other_solution(10,2)
