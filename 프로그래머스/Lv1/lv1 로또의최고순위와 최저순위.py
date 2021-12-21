def solution(lottos, win_nums):
    answer = []
    min_count = 0
    max_count = 0
    count = 0

    # [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19] #본인 로또 당첨로또
    lottos.sort()
    win_nums.sort()

    for i in lottos:

        if i in win_nums:
            count += 1

    max_count = lottos.count(0) + count
    min_count = count

    answer.append(max_count)
    answer.append(min_count)


    for i in range(len(answer)):
        if answer[i] == 6:
            answer[i] = 1
        elif answer[i] == 5:
            answer[i] = 2
        elif answer[i] == 4:
            answer[i] = 3
        elif answer[i] == 3:
            answer[i] = 4
        elif answer[i] == 2:
            answer[i] = 5
        else:
            answer[i] = 6
    print(answer)

    return answer

def solution_others(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

solution(lottos, win_nums)