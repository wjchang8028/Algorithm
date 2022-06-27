import math
t = int(input()) #테스트케이스

for i in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    x_length = x2-x1
    y_length = y2-y1
    dpl = math.sqrt(x_length**2 + y_length**2)


    if dpl == 0 and r1 == r2: #거리도같고 반지름도 같을경우 겹친경우
        print(-1)
    elif abs(r1-r2) == dpl or abs(r1+r2) == dpl: # 한점에서 만남 ( 내접,외접 두가지 경우) abs(r1-r2)가 내접의 경우
        print(1)
    elif abs(r1-r2) < dpl and abs(r1+r2) > dpl: #서로다른 두점 dpl
        print(2)
    else:
        print(0)
    
# r1 + r2 < d 이면 두 원은 서로의 외부에 위치한다.
# r1 + r2 = d 이면 두 원은 외접한다.
# |r1 - r2| < d < r1 + r2 이면 두 원은 서로 다른 두 점에서 만난다.
# |r1 - r2| = d 이면 한 원이 다른 원에 내접한다.
# |r1 - r2| > d, r1 ≠ r2 이면 한 원이 다른 원의 내부에 있다..
    
