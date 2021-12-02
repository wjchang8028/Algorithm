# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000


n = int(input()) #정사각형길이

graph = []
lst = []
cnt = 0

for i in range(n):
    graph.append(list(map(int,input())))


def dfs(x,y):
    
    if x >= n or y >= n or x< 0 or y < 0:
        return False

    if graph[x][y] == 1:
        global cnt
        graph[x][y] = 0 #가본곳은 0찍기
        cnt += 1 #한번 없앨때마다 +1 ->아파트의 갯수
       
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

        return True
    return False

danji = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            lst.append(cnt) #단지 내에 있는 아파트의 수를 리스트에 입력
            danji += 1
            cnt = 0 #새로운 탐색시 cnt값 초기화

print(danji) #총단지수

lst.sort()

for i in lst:
    print(i)
 

