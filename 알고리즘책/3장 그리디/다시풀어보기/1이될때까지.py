#17 ,4 -> 1빼고, 4나누고, 4나눠서 1 총 3번
n,k= map(int,input().split())

count = 0
while True:
    if n % k != 0:
        n -= 1
        count += 1
    elif n % k == 0:
        n = n // k
        count += 1

    if n == 1:
        break
print(count)
