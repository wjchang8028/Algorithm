from itertools import combinations

n, m = map(int,input().split())
card = list(map(int,input().split()))

total = list(combinations(card,3))

max_value = 0

for i in total:
    if max_value < sum(i) <= m:
        max_value = sum(i)

print(max_value)

