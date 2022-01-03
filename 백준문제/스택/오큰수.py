t = int(input())

stack = list(map(int,input().split()))
answer = []


while stack:
    count = 0
    cursor = stack.pop(0)
    
    for i in stack:
        if cursor < i:
            count += 1
        elif cursor >= i:
            count = 0

        if count != 0 :
            answer.append(i)
        else:
            answer.append(-1)
print(answer)
