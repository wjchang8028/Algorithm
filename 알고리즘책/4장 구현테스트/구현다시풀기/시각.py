# 00:00:00 부터 n:59:59 까지 3이 포함된 시각의 수

def solution(n):
    answer = 0
    time = ''
    for hour in range(n+1):
        for min in range(0,60):
            for sec in range(0,60):
                time = str(hour)+str(min)+str(sec)
                
                if '3' in time:
                    answer += 1
    print(answer)
    return answer

solution(5) 
