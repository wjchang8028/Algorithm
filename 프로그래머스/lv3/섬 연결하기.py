def solution(n, costs):
    answer = 0 
    INF = int(1e9)

    print(costs)
    graph = [[INF] * (n+1) for _ in range(n+1)]
    print(graph)

    for a in range(1,n+1):
        for b in range(1,n+1):
            if a == b:
                graph[a][b] = 0
            
    print(graph)


    return answer


solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])