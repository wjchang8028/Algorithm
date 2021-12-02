from collections import deque

n,m,v = map(int,input().split()) #정점수,간선,시작번호

# graph = [[],[2,3,4],[1,4],[1,4],[1,2,3]]
graph = [[] for _ in range(m)]

print(graph)


#그래프형태를 2차원리스트로 삽입
for i in range(n+1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

    
    
print(graph)



def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * m+1
visit = [False] * m+1

dfs(graph,v,visited)
print()
bfs(graph,v,visit)