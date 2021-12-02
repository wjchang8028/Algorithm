# 5 3
# 1 2 5 4 3
# 5 5 6 5 6


import sys

n,k = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    a[i],b[i] = b[i],a[i]
print(a)
print(sum(a))
print()
print(b)
print(sum(b))