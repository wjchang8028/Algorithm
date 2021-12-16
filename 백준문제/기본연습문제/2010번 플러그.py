import sys

n = int(input())

total = 0

for i in range(n):
    a = int(sys.stdin.readline())
    total += a

total = total - (n - 1)

print(total)