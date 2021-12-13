n,m = map(int,input().split())

ball = list(map(int,input().split()))

array = [ball] * n
count = 0

print(array)
for i in range(n-1):
    for j in range(n-1):
        if ball[j] != ball[j+1:]:
            count += 1
print(count)
