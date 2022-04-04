def solution(dirs):
    answer = 0
    move = {'U':(0,1) , 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    movelist = set()
    x,y = (0,0)

    for i in dirs:
        nx,ny = x + move[i][0] , y + move[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            movelist.add((x,y,nx,ny)) # 같은 목적지 좌표지만 방향이 다른 경우
            movelist.add((nx,ny,x,y))
            x,y = nx,ny 

    answer = len(movelist) // 2
    print(answer)
    return answer

solution("ULURRDLLU")
solution("LULLLLLLU")