t = int(input())
stack = []

for i in range(t):
    n = int(input())

    if n == 0:
        stack.pop()
    else:
        stack.append(n)

if len(stack) == 0:
    print(0)
else:
    print(sum(stack))