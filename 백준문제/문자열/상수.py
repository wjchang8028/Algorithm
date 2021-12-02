a,b = map(str,input().split())

# a = a[2]+a[1]+a[0]
# b = b[2]+b[1]+b[0]

a = a[::-1] #arr[a:b:c] -> a부터 b까지 c순으로 배열화 -1은 역순
b = b[::-1]

# if int(a) > int(b):
#     print(a)
# else:
#     print(b)

print(max(int(a),int(b)))