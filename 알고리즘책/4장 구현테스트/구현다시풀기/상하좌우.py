# n * n 크기 지도에서 이동을 했을때 마지막 좌표값 .
# 시작은 1,1 부터 끝은 n,n

def solution(n,move):
    answer = 0
    x,y = 0, 0 #시작위치

    for i in move:
        if i == 'R':
            if y < n-1:
                y = y + 1
            else:
                pass

        elif i == 'L':
            if 0 < y:
                y = y - 1
            else:
                pass

        elif i == 'U':
            if 0 < x:
                x = x - 1
            else:
                pass

        elif i == 'D':
            if x < n-1:
                x = x + 1
            else:
                pass

    x += 1
    y += 1

    print("({} , {})".format(x,y))
            
    return answer

def other_solution(n,move):
    answer = 0
    # 상 하 좌 우
    dx = [-1 , 1 , 0 , 0]
    dy = [0 , 0 , -1, 1]
    direction = ['U','D','L','R']

    x,y = 1,1
    for i in move:
        for j in range(len(direction)):
            if i == direction[j]:
                nx = x + dx[j]
                ny = y + dy[j]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x = nx
        y = ny

    print(x,y,sep=',')

    return answer

n = 5
move = ['R','R','R','U','D','D','L','L','L','L','L','U']
solution(n,move)
other_solution(n,move)

