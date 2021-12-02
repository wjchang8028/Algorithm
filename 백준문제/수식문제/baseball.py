t = int(input())
yscore = 0
kscore = 0


for i in range(t):
    for game in range(9):
        y,k = map(int,input().split())

        yscore += y
        kscore += k
    
    if yscore > kscore :
        print("Yonsei")
    elif kscore > yscore:
        print("Korea")
    else:
        print("Draw")
