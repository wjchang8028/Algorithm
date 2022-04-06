n = int(input())
answer = []
for i in range(n+1):
    t = str(i)
    total = 0
    for j in range(len(t)):
        total += int(t[j])
    
    if i + total == n:
        answer.append(i)

if len(answer) == 0:
    print(0)
else:
    print(min(answer))
    