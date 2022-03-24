

def solution(N, number):
    possible_set = [0,[N]]
    if N == number:
        return 1

    for i in range(2,9):
        case_set = []
        basic_num = int(str(N) * i)
        case_set.append(basic_num)
        print(case_set)

        for i_half in range(1, i//2+1):
            for x in possible_set[i_half]:
                for y in possible_set[i-i_half]:

                    case_set.append(x+y)
                    case_set.append(x-y)
                    case_set.append(x*y)
                    case_set.append(y-x)

                    if y != 0:
                        case_set.append(x/y)
                    if x != 0:
                        case_set.append(y/x)
            if number in case_set:
                return i
            possible_set.append(case_set)

    return -1

solution(5,12)
solution(2,11)

def solution2(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            else:
                triangle[i][j] = max(triangle[i-1][j-1] , triangle[i-1][j]) + triangle[i][j]

    print(triangle)
    answer = max(triangle[len(triangle)-1])
    print(answer)
    return answer

# solution2([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])