def solution(line):
    answer = []

    for i in range(len(line)):
        for j in range(i,len(line)):
            if line[i][0] == -1 * line[j][0]:
                for x in range(1000):
                    line[i][0] * x 
    return answer

solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])