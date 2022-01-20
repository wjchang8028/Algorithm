import sys
input = sys.stdin.readline
INF = int(1e9)

t = int(input()) # testcase

for i in range(t): 
    N,M,K = map(int,input().split()) # 공항, 총비용, 티켓수

    graph = [[INF]*(N+1) for _ in range(N+1)]

    for _ in range(K):
        start,end,cost,time = map(int,input().split()) # 출발공항, 도착공항, 비용, 소요시간

        graph[start][end] = cost
        graph[end][start] = cost
      

    for k in range(1,N+1):
        for a in range(1,N+1):
            for b in range(1,N+1):
                if a == b:
                    graph[a][b] = 0
                else:
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                
    

    if graph[1][N] > M:
        print("Poor KCM")
    elif graph[1][N] <= M:
        print(graph[1][N])


