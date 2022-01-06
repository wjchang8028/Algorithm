# 열 column (y) 행 row (x) 일반적인 유클리드기하의 행렬과는 축이 바뀜 . 쉽게보기위해 고개를 오른쪽으로 90도 돌려서 보면됨

# 동(0,1)
# 북(-1,0)
# 서(0,-1)
# 남(1,0)

#dx [0, -1, 0, 1]
#dy [1, 0, -1, 0] 



# 5 * 5 정방행렬
column = 5
row = 5
matrix = [[0] * column for _ in range(row)]

for i in range(column):
    for j in range(row):
        matrix[i][j] = (i,j)
print(matrix)

# 현재 위치 2,2 일때
dx = [0,-1,0,1]
dy = [1,0,-1,0]

#초기좌표가
x,y = 2,2

for i in range(4):
    # 다음위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny) # (2,3) , (1,2) , (2,1) ,(3,2) 로 이동. 차례로 동 북 서 남 으로 감