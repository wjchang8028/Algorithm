temp = []
def dfs(graph,v,visited):
    
    visited[v] = True
    print(v,end=' ')
    temp.append(v)
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def solution(n,computers):
    n = 3
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            computers[i][i] = 0
            if computers[i][j] == 1:
                graph[i].append(j+1)
            
    print(graph)
    visited = [False] * (n+1)

    dfs(graph,1,visited)
    a = max(temp)
    print(a)
    answer = n - a
    print(answer)
    return answer

solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])