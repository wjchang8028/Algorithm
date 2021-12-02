n = int(input())
lst = []
for i in range(n):
    cute = int(input())
    lst.append(cute)

iscute = lst.count(1)
isNotcute = lst.count(0)

if isNotcute > iscute:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")