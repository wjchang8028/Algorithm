#인접행렬 [[0,7,5],[7,0,무한],[5,무한,0]]

graph = [[] for _ in range(3)] #행이 3개인 2차원배열 생성

print(graph)

#노드 0에 연결된 노드 정보 저장 (노드,거리)
graph[0].append((1,7))
graph[0].append((2,5))

#노드 1에 연결된 노드 정보 저장 (노드,거리)
graph[1].append((0,7))

#노드 2에 연결된 노드 정보 저장 (노드,거리)
graph[2].append((0,5))

print(graph)