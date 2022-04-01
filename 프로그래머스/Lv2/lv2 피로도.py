def solution(k, dungeons):
    answer = 0

    dungeons.sort(key=lambda x: (x[1]-x[0],x[1])) # 필요 피로도와 소모피로도의 차이가 큰것 
    for i in range(len(dungeons)):
        if k >= dungeons[i][0]: # 현재 피로도가 입장조건에 맞다면
            k -= dungeons[i][1]
            answer += 1
        else: # 입장 조건에 맞지 않는다면
            continue
    print(answer)

    return answer

solution(80, [[80,20],[50,40],[30,10]])
solution(16, [[4,1],[8,2],[12,3],[16,4]])

answer = 0
visited = []

def dfs(k,cnt,dungeons):
    global answer

    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons)
            visited[i] = 0

def other_solution(k,dungeons):
    global answer,visited
    visited = [0] * len(dungeons)

    dfs(k,0,dungeons)
        
    print(answer)
    return answer
other_solution(80, [[80,20],[50,40],[30,10]])
other_solution(16, [[4,1],[8,2],[12,3],[16,4]])
