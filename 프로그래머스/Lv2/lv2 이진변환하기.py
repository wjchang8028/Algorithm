import sys

sys.setrecursionlimit(10**6)
zero_count = 0
round = 0

def reclusion(s):
    global zero_count,round

    round += 1
    temp = ''
    for i in s:
        if i == '1':
            temp += i
        else:
            zero_count += 1
    print(temp , zero_count) # 0 제거

    length = len(temp)

    a = str(bin(length)[2:])
    print(a)

    if a == '1':
        return round
    else:
        return reclusion(a)


def solution(s):
    global zero_count,round
    answer = []

    reclusion(s)
    answer.append(round)
    answer.append(zero_count)

    return answer

solution("110010101001")
solution("01110")

def other_solution(s):
    cnt, zero_del = 0,0

    while s != '1':
        cnt += 1
        num = s.count('1')
        zero_del += len(s) - num
        s = bin(num)[2:]
    answer = [cnt,zero_del]
    print(answer)
    return answer

other_solution("110010101001")
other_solution("01110")
