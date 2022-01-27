n = int(input())

array = list(map(int,input().split(" ")))
array.sort()
print(array[(n-1)//2])


# 9
# 1 3 5 7 8 15 17 20 21
# 답 : 7