def solution(N, number):
    answer = 0
    cal = ['+','-','//','*']




    return answer

solution(5,12)

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

solution2([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])