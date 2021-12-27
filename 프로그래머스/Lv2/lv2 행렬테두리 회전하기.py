def solution(rows, columns, queries):
    answer = []

    array = [[0 for col in range(columns)] for row in range(rows)]
    print(array)
    t = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t += 1
    print(array)

    print("==============================================")

    matrix = [[0]* columns] * rows
    print(matrix)
    number = 1

    for row in range(rows):
        for col in range(columns):
            matrix[row][col] = number
            number += 1
    
    print(matrix)

    return answer

queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(6,6,queries)