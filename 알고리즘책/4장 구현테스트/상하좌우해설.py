import time


n = int(input())

start = time.time()

x, y = 1, 1

plans = input().split()

dx = [0,0,-1,1]
dy = [1,-1,0,0]
move = ['r','l','u','d']

for plan in plans:

    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx > n or nx < 1 or ny > n or ny < 1:
        continue

    x,y =nx,ny

print(x,y)
print("걸린시간 : " ,time.time() - start)