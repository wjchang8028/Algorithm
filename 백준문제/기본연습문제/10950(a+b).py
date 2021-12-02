#case = int(input())


# for i in range(1,case+1):
#     a,b = map(int,input().split())
#     print(a+b)

import sys

case = int(input())
for i in range(case):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)
