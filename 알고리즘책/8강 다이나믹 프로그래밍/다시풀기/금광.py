n,m =  3,4
mine = [[1,3,3,2],[2,1,4,1],[0,6,4,7]]
print(mine)
temp = []

for j in range(1,m):
    for i in range(n):

        #왼쪽위에서 오는경우
        if i == 0 : 
            left_up = 0
        else:
            left_up = temp[i-1][j-1]

        #왼쪽아래에서 오는경우
        if i == n-1:
            left_down = 0
        else:
            left_down = temp[i+1][j-1]
        
        #왼쪽에서 오는경우
        left = temp[i][j-1]
        temp[i][j] = temp[i][j] + max(left_up,left_down,left)
    result = 0

    for i in range(n):
        result = max(result,temp[i][m-1])
    