import sys
n = int(input())

nlist = sys.stdin.readline().split()

m = int(input())

mlist = sys.stdin.readline().split()

for i in mlist:
    if i in nlist:
        print(1)
    else:
        print(0)
