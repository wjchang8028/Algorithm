# 체스판에서 나이트가 갈 수 있는 경우의 수 x축은 1~8까지 y축은 a~ h 까지
# 8*8체스판

def solution(location):
    answer = 0
    temp = []

    knight_move = ['1번','2번','3번','4번','5번','6번','7번','8번'] #for문으로 방식확인용
    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [1,2,2,1,-1,-2,-2,-1]

    for i in range(len(knight_move)):
        x,y = int(location[1]),ord(location[0])-96
        nx = x + dx[i]
        ny = y + dy[i] 

        if nx < 1 or ny < 1 or nx > 8 or ny > 8:
            continue
        answer += 1

    print(answer)
    return answer

def other_solution(location):
    row = int(location[1])
    column = int(ord(location[0])) - int(ord('a')) + 1

    #나이트가 이동하는 8가지
    steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

    result = 0

    for step in steps:
        next_row = row + step[0]
        next_col = column + step[1]

        if 1 <= next_row <= 8 and 1 <= next_col <= 8:
            result += 1
    print(result)
    return result

 
solution('h8')
other_solution('h8')
