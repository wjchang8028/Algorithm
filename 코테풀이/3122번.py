# 재 풀이
from itertools import combinations, permutations
imsi = []

def dfs(graph,v,visited):  
    global imsi
    
    visited[v] = True
    imsi.append(v)
    for i in graph[v]:
        if not visited[i]: 
            dfs(graph,i,visited) 


def solution(n, edges):
    answer = 0
    temp = []
    visited = [False] * (n+1)

    for i in range(len(edges)):
        for j in range(len(edges[i])):
            temp.append(edges[i][j])
    arr = list(set(temp))
    # print(arr)

    a = list(combinations(arr,3))
    print(a)

    matrix = [[] for _ in range(5)]

    for i in range(len(edges)):
        matrix[edges[i][0]].append(edges[i][1])
        matrix[edges[i][1]].append(edges[i][0])
    print("행렬",matrix)
    
    for i in range(len(a)):
        dfs(matrix,a[i][0],visited)
        visited = [False] * (n+1)

    print(imsi.count(0))
        
    
    return answer

solution(5,[[0,1],[0,2],[1,3],[1,4]])

solution(4,[[2,3],[0,1],[1,2]])
