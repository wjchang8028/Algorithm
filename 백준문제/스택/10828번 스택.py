t = int(input())
stack = []
order = ['push', 'pop','top','empty','size']

for i in range(t):
    order = input()

    if order[:4] == 'push':
        stack.append(order[5:])

    elif order == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

    elif order == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif order == 'size':
        print(len(stack))




    

