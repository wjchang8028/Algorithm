t = int(input())

for i in range(t):

    n = int(input())
    d = [0] * (n+2)

    d[0] = 1
    d[1] = 1
    d[2] = 1
    
    for i in range(3,n+1):
        d[i] = d[i-3] + d[i-2]

    print(d[n-1])
