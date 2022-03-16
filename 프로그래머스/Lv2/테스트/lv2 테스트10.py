def first_solution(n):
    answer = 0
    value = bin(n)[2:]
    print(value)

    count = value.count('1')
    print(count)

    for i in range(n+1, 1000001):
        cnt = bin(i)[2:]
        if cnt.count('1') == count:
            answer = i
            break
    
    print(answer)
    return answer

# first_solution(78)
# first_solution(15)

def solution(s):
    answer = ''
    lst = list(map(int,s.split(' ')))
    max_value = str(max(lst))
    min_value = str(min(lst))

    answer = max_value + ' ' + min_value
    print(answer)
    return answer

solution("1 2 3 4")
solution("-1 -2 -3 -4")
solution("-1 -1")