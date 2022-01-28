
n = int(input())
stages = list(map(int,input().split(" ")))
stages.sort()
print(stages)

def solution(N, stages):
    result = {}
    denominator = len(stages) # 총 유저
    for stage in range(1, N+1):
        if denominator != 0: # 유저가 있다면
            count = stages.count(stage) # 현재 스테이지에 머물러있는 사람수
            result[stage] = count / denominator # 현재스테이지 = 머물러있는사람수 / 총 유저
            denominator -= count # 총 유저 - 현재 스테이지 유저수
        else: # 유저가 더이상없으면 0
            result[stage] = 0  
    print(result)
    return sorted(result, key=lambda x : result[x], reverse=True)

solution(n,stages)
# 5
# 2 1 2 6 2 4 3 3