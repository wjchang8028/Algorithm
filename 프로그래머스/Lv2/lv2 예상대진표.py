# n명 참가 a번째 선수와 b번째 선수 만나는 라운드

import sys
sys.setrecursionlimit(10**6)

answer = 0
def bisect(player,a,b):
    global answer
    answer += 1

    for i in range(len(player)):
        player[i][0] //= 2
    
    
    if player[a-1][0] == player[b-1][0]:
        return player
    else:
        return bisect(player,a,b)


def solution(n,a,b):
    global answer
    player = [[i-1,i] for i in range(1,n+1)]
    bisect(player,a,b)

    print(answer)
    return answer

solution(8,4,7)