
def solution(s):
    answer = ''
    a = list(s.split(" "))
    print(a)
    b = []
    for i in a:
        b.append(list(i))

    for i in range(len(b)):
        for j in range(len(b[i])):
            if j % 2 == 0:
                b[i][j] = b[i][j].upper()
                answer += b[i][j]
            else:
                b[i][j] = b[i][j].lower()
                answer += b[i][j]
        answer += ' '
    c = list(answer)
    c.pop()
    
    answer = "".join(c)
    
    return answer

s = "try hello world "
solution(s)