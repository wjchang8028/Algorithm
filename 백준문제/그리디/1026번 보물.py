t = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)
sum = 0

for i in range(t):
    sum += a[i] * b[i]
print(sum)
