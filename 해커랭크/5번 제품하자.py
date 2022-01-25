from imp import source_from_cache


n = int(input())
m = int(input())
graph = [] * n 
for i in range(n):
    graph.append(list(map(int,input().split())))

print(graph) # 판

def solution(graph):
    width = len(graph)
    height = len(graph[0])

    for i in range(1,width):
        for j in range(1,height):
            if graph[i][j] == 1:
                graph[i][j] = min(graph[i-1][j],graph[i][j-1],graph[i-1][j-1]) + 1

    print(max([item for row in graph for item in row])) 
    return max([item for row in graph for item in row])
            
solution(graph)
        
# 입력예제

# 3
# 3
# 1 1 1
# 1 1 0
# 1 0 1