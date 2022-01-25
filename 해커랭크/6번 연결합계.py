# 노드 그룹의 깊이를 각각 제곱근 후 올림하여 모두 더하는 문제
# ex) 1 - 2 - 3 - 4 -5 (그룹1) , 7 - 8 (그룹2) , 6 9 10(그룹3,4,5)
# 5의제곱근의 올림 + 2의제곱근의 올림 + ( 1 의 제곱근의 올림 * 3) = 8

import math

def dfs(graph,v,visited):
    visited[v] = True
    # print(v,end=" ")
    global count
    count += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph = []
graph_from = []

n , m = map(int,input().split()) # 노드, 간선
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int,input().split()) # 그래프
    graph_from.append(start)
    graph[start].append(end)

temp = []

for i in graph_from:
    count = 0
    dfs(graph,i,visited)
    temp.append(count)

print(graph)
print(temp)

total = 0
for i in temp:
    total += math.ceil(i**0.5)
print(total)

# 입력예제

# 10 5
# 1 2
# 1 3
# 2 4
# 3 5
# 7 8

# 4 2
# 1 2
# 1 4