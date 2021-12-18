t = int(input())

for i in range(t):
    candy,bro = map(int,input().split())
    print("You get {} piece(s) and your dad gets {} piece(s)." .format(candy//bro , candy % bro))