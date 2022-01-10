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

start_node = 1 # 시작되는 노드
visited = [False] * 9 # 총 노드 + 1 

#DFS 구현법 (깊이 탐색. 인접 노드 중에서 가장 작은 수부터. (노드별로 정렬이 필요해보임))
def dfs(graph,start_node,visited):
    visited[start_node] = True #방문한곳 => True

    print(start_node,end=' ')

    for i in graph[start_node]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,start_node,visited)

start_node = 1
visited = [False] * 9 # 총 노드 + 1

print()
#BFS 구현법 (너비 우선 탐색, 가장 가까운 노드부터 탐색 (큐)를 사용함)
from collections import deque
def bfs(graph,start_node,visited):
    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
bfs(graph,start_node,visited)

