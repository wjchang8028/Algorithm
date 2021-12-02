import sys

n = int(sys.stdin.readline().rstrip())

nlist = sys.stdin.readline().split()

m = int(sys.stdin.readline().rstrip())

mlist = sys.stdin.readline().split()


for i in mlist:
    if i in nlist:
        print('yes',end=' ')
    else:
        print('no',end= ' ')