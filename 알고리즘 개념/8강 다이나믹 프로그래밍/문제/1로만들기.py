x = int(input())

d = [0] * 30001

# def func(x): 잘못된 함수
#     if d[x] == 1:
#         return 1
#     if x % 5 == 0:
#         d[x] = d[x] //5
#     elif x % 3 == 0:
#         d[x] = d[x] // 3
#     elif x % 2 == 0:
#         d[x] = d[x] // 2
#     d[x] = d[x-1] - 1

for i in range(2, x+1):
    #현재의 수에서 1을 빼는경우
    d[i] = d[i-1] + 1

    #현재의 수에서 2를 나누어 떨어지는경우
    if i % 2 == 0:
        d[i] = min(d[i],d[i // 2]+1)

    #현재의 수에서 3를 나누어 떨어지는경우
    if i % 3 == 0:
        d[i] = min(d[i],d[i // 3]+1)

    #현재의 수에서 5를 나누어 떨어지는경우
    if i % 5 == 0:
        d[i] = min(d[i],d[i // 5]+1)
print(d[x])