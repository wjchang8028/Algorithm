def solution(n, clockwise): # 구현
    answer = [[]]
    matrix = [[0 for _ in range(n)] for _ in range(n)] # 2차원행렬

    if clockwise == True: # 시계방향 소용돌이
        value = 0

        for i in range(n):
            for j in range(n):
                value += 1
                matrix[i][j] = value

                if j == n-1:
                    value = 1
                    matrix[i][j] = value
                    value += 1
                
                if i == n - 1:
                    value = 1
                    matrix[j][i] = value
                    value += 1
                

    
        

    # else: # 반시계 소용돌이


    print(matrix)
    return answer

solution(5,True)
