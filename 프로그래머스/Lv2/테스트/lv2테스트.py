def solution(s):
    answer = ''
    array = list(map(int,s.split()))
    print(array)

    a = min(array)
    b = max(array)
    answer = str(a)+" "+str(b)
    print(answer)
    return answer

s = "-1 2 3 4"
solution(s)