t = int(input())

stack = list(map(int,input().split()))

answer = []

for i in range(t):
    while answer:
        if stack[i] > stack[answer[-1]]: 
            stack[answer.pop()] = stack[i]
        else:
            answer.append(i)
            break
    
    if not answer:
        answer.append(i)
for i in answer:
    stack[i] = -1
        

print(*stack)
