from collections import deque

#BFS메서드 정의
def bfs(graph,start,visited):
    #큐 구현을위해 deque라이브러리 사용
    queue = deque([start])
    print(queue)

    #현재 노드를 방문처리
    visited[start] = True

    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v,end=' ')

        #해당 원소와 연결된, 아직 방문하지않은 원소들을 큐에 삽입
        for i in graph[v]: #그래프에 연결되어있는 노드들 수 만큼 반복 graph[1] = [2,3,8]이 연결되어있으므로 3번반복.
            if not visited[i]: #방문하지않았다면
                queue.append(i) #큐에 삽입
                visited[i] = True #방문기록 찍음


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원리스트)

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
bfs(graph,1,visited)