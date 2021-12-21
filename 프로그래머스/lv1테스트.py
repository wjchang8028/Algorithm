def solution(n, m):
    answer = []
    temp = []
    for i in range(1,1000001):
        if n % i == 0 and m % i == 0:
            temp.append(i)
    a = max(temp)
    b = a * (n // a) * (m // a)
    answer.append(a)
    answer.append(b)

    print(answer)
    return answer

solution(100,12)