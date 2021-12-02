# n = int(input())

# lst = []
# namelst = []
# for i in range(n):
#     p = int(input())

#     for j in range(p):
#         cost,name = input().split()
#         lst.append(int(cost))
#         namelst.append(name)

#     for i in range(len(lst)):
#         if max(lst) == lst[i]:
#             a = i
#     print(namelst[a])
#     namelst.clear()
#     lst.clear()
    

import sys
s = sys.stdin.readline
for _ in range(int(s())):
    maxprice = -1
    for _ in range(int(s())):
        p, n = s().split()
        p = int(p)
        if p > maxprice:
            maxprice = p
            maxname = n
    print(maxname)
        