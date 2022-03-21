def solution(n, left, right):
    answer = []
    temp = []

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for i in range(n):
            for j in range(n):
                if i == x or j == x:
                    matrix[i][j] = x+1


    print(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            temp.append(matrix[i][j])
    
    answer = temp[left:right+1]

    print(answer)
    return answer

solution(3,2,5)
solution(4,7,14)
solution(5,8,16)
solution(6,7,14)

def other_solution(n,left,right):
    answer = []

    for i in range(left,right+1):
        answer.append(max(i // n , i % n) + 1)

    print(answer)
    return answer

other_solution(4,7,14)

