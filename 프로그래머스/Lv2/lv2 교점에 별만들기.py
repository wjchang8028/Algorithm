from itertools import combinations

# solutio 1 : combinations 사용
def solution(line):
    answer = []

    INF = 100000

    intersections=[]

    max_x=-INF
    min_x=INF
    max_y=-INF
    min_y=INF

    for first,second in combinations(line,2):
        a,b,e = first
        c,d,f = second

        mod = (a*d - b*c)
        if mod==0:
            continue

        x = (b * f - e * d) / mod
        y = (e * c - a * f) / mod

        if x!=int(x) or y!=int(y):
            continue
        x=int(x)
        y=int(y)

        intersections.append((x,y))

        max_x = max(x, max_x)
        min_x = min(x, min_x)
        max_y = max(y, max_y)
        min_y = min(y, min_y)

    # 너비와 높이를 계산 후, 별을 찍습니다.
    h=max_y-min_y+1
    w=max_x-min_x+1

    matrix = [['.'] * w for _ in range(h)]

    for x,y in intersections:
        matrix[max_y-y][x-min_x] = '*'

    for i in range(h):
        answer.append("".join(matrix[i]))

    print(answer)
    return answer


solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
solution([[[1, -1, 0], [2, -1, 0], [4, -1, 0]]])