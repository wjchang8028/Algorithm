def hanoi(input,a,b,c):
    if input == 1:
        move.append([a,c]) # 1에서 3번으로 이동한것

    else:
        hanoi(input-1,a,c,b) #1번원판을 3번으로
        move.append([a,c])
        hanoi(input-1,b,a,c) #2번원판을 3번으로

move=[]

hanoi(int(input()),1,2,3)

print(len(move))
for i in range(len(move)):
    print(move[i][0],move[i][1])