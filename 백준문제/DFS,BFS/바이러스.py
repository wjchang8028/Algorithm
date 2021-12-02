node = int(input())
network = int(input())

graph = [[0] * (node+1)  for _ in range(node+1)]

print(graph)
for i in range(network):
    p1,p2 = map(int,input().split())
    graph[p1][p2] = graph[p2][p1]=1
   
# print(graph)

viruslist = []

def dfs(start,visited=[]):
    visited.append(start)
    viruslist.append(start)

    for i in range(len(graph[start])):
        if graph[start][i] == 1 and (i not in visited):
            dfs(i,visited)

dfs(1)

print(len(viruslist)-1)
