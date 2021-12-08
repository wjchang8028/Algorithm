def solution(board, moves):
    answer = 0
    box = [] 
    
    for i in moves: #moves 마다 반복됨
        for j in range(len(board)): #n * n 행렬이기때문
            if board[j][i-1] != 0: # moves의 값에서 돌리다가 0이아니면
                box.append(board[j][i-1]) #box라는 스택에 값을 저장해주고
                board[j][i-1] = 0 #빼낸곳은 0으로 초기화
            
                if len(box) > 1: #박스안에 있는 인형수가 2개 이상이면
                    if box[-1] == box[-2]: #맨 뒤랑 그 앞이 같다면
                        box.pop(-1) # 뒤에서 하나씩 없애주기
                        box.pop(-1)
                        
                        answer += 2
                break
    print(answer)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board,moves)