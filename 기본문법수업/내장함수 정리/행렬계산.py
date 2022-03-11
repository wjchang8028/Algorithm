def productMatrix(A,B):
    answer = []
    for i in range(len(A)):
        a = []
        for j in range(len(B[0])):
            temp = 0
            for k in range(len(A[0])):
                temp += (A[i][k] * B[k][j])
            a.append(temp)
        answer.append(a)
    
    print(answer)
    return answer
    
productMatrix([[1, 4], [3, 2], [4, 1]] ,[[3, 3], [3, 3]])
productMatrix([[2, 3, 2], [4, 2, 4], [3, 1, 4]]	,[[5, 4, 3], [2, 4, 1], [3, 1, 1]])
productMatrix([[1,3,2],[1,3,3]] , [[1,2],[4,5],[3,6]])