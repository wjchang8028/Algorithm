def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]



def solution(n, t, m, p):
    answer = ''
    temp = ''
    for i in range(t * m):
        temp += convert(i,n)
        
    arr = list(temp)

    for i in range(len(arr)):

        if i % m == p - 1:
           
            answer += arr[i]
        
        if len(answer) == t:
            break

    print(answer)

    return answer

n = 2
t = 4
m = 2
p = 1
solution(n,t,m,p)
