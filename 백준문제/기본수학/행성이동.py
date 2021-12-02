import sys
case = int(input())

for i in range(case):
    x , y = map(int,sys.stdin.readline().split())
    k = 0
    sum = 0
    cnt = 1
    if x == 0:
        distance = y-x
    else:
        distance = y-x-1 #거리

    for j in range(1000):
        k+=1
        sum += k
        cnt += 1
        if sum >= distance:
            break
    print(cnt)
    
    