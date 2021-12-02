n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input()))) #얼음판 받기

print(graph)

def dfs(x,y): #dfs 는 재귀방식
    if x <= -1 or x>=n or y<=-1 or y>=m: #범위 초과시
        return False
    
    if graph[x][y] == 0: #얼음판에서 0이 있으면
        graph[x][y] = 1 #방문지 등록하고

        dfs(x,y-1)#상
        dfs(x,y+1)#하
        dfs(x-1,y)#좌
        dfs(x+1,y)#우 탐색

        return True #0 이 있으면 계속 true
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)
    
