# 다시 풀기
n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))
array.sort()

total = 0

for i in range(len(array)-1):
    array[i+1] = array[i]+array[i+1]
    total += array[i+1]
print(total)

