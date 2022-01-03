def rotate_matrix_90(a):
    n = len(a) #행의 길이
    m = len(a[0]) #열의 길이

    result = [[0] * n for _ in range(m)] 

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

#자물쇠의 중간부분이 전부 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length,lock_length * 2):
        for j in range(lock_length,lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key,lock):
    n = len(lock)
    m = len(key)

    #자물쇠 크기를 3배로 늘림
    new_lock = [[0] * (n*3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 4가지 방향 확인
    for rotation in range(4):
        key = rotate_matrix_90(key) #열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                #자물쇠에 열쇠 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                
                #새로운 자물쇠에 열쇠가 맞는지 검사
                if check(new_lock) == True:
                    print("맞음")
                    return True
                
                #자물쇠에서 열쇠다시빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    print("틀림")
    return False



key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]
solution(key,lock)