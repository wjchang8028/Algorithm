timer = [300,60,10]
count = [0 , 0 , 0]
def solve(t):
    for i in range(len(timer)):

        count[i] = t // timer[i]
        t = t % timer[i]
    return t
    
t = int(input()) #시간

solve(t)


if solve(t) == 0:
    print (count[0],count[1],count[2])
else:
    print(-1)
