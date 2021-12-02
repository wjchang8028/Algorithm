n = int(input())

array = []
for i in range(n):
    a = int(input())
    array.append(a)

array.sort(reverse=True)
# array = sorted(array,reverse=True)

print(array)