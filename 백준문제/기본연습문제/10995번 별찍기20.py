t = int(input())

for i in range(t):
    if i % 2 == 0:
        for j in range(t):
            print("* ",end="")
    else:
        for j in range(t):
            print(" *",end="")
    print()