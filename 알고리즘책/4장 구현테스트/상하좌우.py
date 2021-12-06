import time


n = int(input()) # n * n 크기의 지도 생성

start = time.time()

#시작은 왼쪽위 1,1 오른쪽아래 n,n

movedata = input().split()

#시작좌표
x = 1
y = 1

# print(movedata) 입력값 리스트

for i in movedata:

    if i == 'r':
        y += 1
        if y > n:
            y = y - 1
        

    elif i == 'l':
        y -= 1
        if y < 1:
            y = y + 1
        

    elif i == 'd':
        x += 1
        if x > n:
            x = x - 1
        

    elif i == 'u':
        x = x - 1
        if x == 0:
            x = x + 1
        

print(x , y, sep=",")
print("걸린시간 : " ,time.time()-start)
