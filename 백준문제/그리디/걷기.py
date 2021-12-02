x,y,w,s = map(int,input().split())

move = [(1,0),(0,1),(1,1),(1,-1)] #옆 위 대각위 대각아래

startX=0
startY = 0 #시작 x,y좌표

countx = 0
county = 0

for i in range(x):
    countx += 1
    startX += 1

    if startX == x:
        break
for i in range(y):
    county += 1
    startY += 1

    if startY == y:
        break

print("총 경우의 수 : ",countx + county)


           