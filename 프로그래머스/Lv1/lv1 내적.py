def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer

def usingzip(a,b): #zip()참고
    answer = 0
    for a,b in zip(a,b):
        answer += a*b
    
    return answer

a = [1,2,3,4]
b = [-3,-1,0,2]

print(solution(a,b))
print(usingzip(a,b))
