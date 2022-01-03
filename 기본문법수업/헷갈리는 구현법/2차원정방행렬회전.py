#2차원 리스트 90도 회전

def rotate_matrix_90(a):
    n = len(a) #행의 길이
    m = len(a[0]) #열의 길이

    result = [[0] * n for _ in range(m)] # [[0] * n * m] 으로 하면 주소값이 복사되는 얕은복사 형태라 값이 완전히 이상하게 나옴

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    
    print(result)

a = [[1,2,3],[4,5,6],[7,8,9]]
rotate_matrix_90(a)