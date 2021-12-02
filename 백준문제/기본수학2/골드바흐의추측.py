a = [0,0]+[1]*10000

prime = []

for j in range(2,101):
    if a[j]:
        prime.append(j)
        for k in range(j*2,10001,j):
            a[k] = 0



t = int(input())

for i in range(t):
    n = int(input()) #짝수 . 골드바흐파티션값
    
    x = n //2
    y = x

    for j in range(10000):
        if a[x] and a[y]:
           
            print(x,y)
            break
        x -= 1
        y += 1
