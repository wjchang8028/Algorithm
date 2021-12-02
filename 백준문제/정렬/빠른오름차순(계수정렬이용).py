import sys

n = int(sys.stdin.readline().rstrip())

array = []

for i in range(n):
    array.append(int(sys.stdin.readline().rstrip()))
# print(array)

count = [0] * (len(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)