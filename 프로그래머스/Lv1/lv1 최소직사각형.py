def solution(sizes):
    answer = 0
    long =[]
    short = []

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            long.append(sizes[i][1])
            short.append(sizes[i][0])
        else:
            long.append(sizes[i][0])
            short.append(sizes[i][1])
    answer = max(long) * max(short)
    print(answer)
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
solution(sizes)