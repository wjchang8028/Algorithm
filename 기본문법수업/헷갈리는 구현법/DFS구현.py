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
] # 자체적으로 줄 수도 있고 

edges = [[0,1],[0,2],[1,3],[1,4],[5,6]] # 2차원 배열형태로 줄 수도 있음

def dfs(graph,start_node,end_node,visited):
    visited[start_node] = True 
    
    # print(start_node,end_node)

    for i in graph[start_node]:
        if not visited[i]:
            dfs(graph,i,end_node,visited)


def solution(edges):
    matrix = [[] for _ in range(max(max(edges))+1)] # 그래프화 
    distance = 0
    for i in range(len(edges)): # 2차원배열을 그래프형태로 변환
        matrix[edges[i][0]].append(edges[i][1])
        matrix[edges[i][1]].append(edges[i][0])
    print("행렬 : ",matrix)

    visited = [False] * (max(max(edges)) + 1) #2차원배열에서 가장 큰 값은 max를 두번

    dfs(matrix,1,6,visited)
    print(visited)

solution(edges)