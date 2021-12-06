#dfs정의

def dfs(graph,v,visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v,end=' ')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

#각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원리스트)

graph = [
    [], #0과연결된 노드
    [2,3,8], #1과 연결된 노드
    [1,7], #2와 연결된 노드
    [1,4,5], #3과 연결된 노드
    [3,5], #4와 연결된 노드
    [3,4], #5와 연결된 노드
    [7], #6과 연결된 노드
    [2,6,8], #7과 연결된 노드
    [1,7] #8과 연결된 노드
]

#각 노드가 방문한 정보를 리스트 자료형으로 표현(1차원리스트)
visited = [False] * 9

#정의된 dfs 함수 호출
dfs(graph,1,visited)