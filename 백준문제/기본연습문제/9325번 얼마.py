t = int(input())


for i in range(t):
    total = int(input()) #차 값

    t2 = int(input())
    
    for j in range(t2):
        option , cost = map(int,input().split()) #옵션과 비용
        total += option * cost
    
    print(total)


