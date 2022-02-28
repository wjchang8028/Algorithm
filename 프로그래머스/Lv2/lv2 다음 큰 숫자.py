def solution(n):
    answer = 0
    binary = bin(n)
    
    arr = list(binary[2:])

    cnt = arr.count('1')

    for i in range(n+1,10000000):
        binary = bin(i)
        if binary[2:].count('1') == cnt:
            answer = int(binary,2)
            break
    print(answer)
        

    return answer

n=78
solution(n)