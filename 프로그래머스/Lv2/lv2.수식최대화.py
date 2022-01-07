from itertools import permutations
def solution(expression):
    symbol = ['+', '-', '*']
    answer = []

    for per in permutations(symbol):
        f, s = per[0], per[1]
        print(f,s)
        lst = []
        for e in expression.split(f):
            temp = [f"({i})" for i in e.split(s)]
            lst.append(f'({s.join(temp)})')
            print(lst)
        answer.append(abs(eval(f.join(lst))))
    
    print(max(answer))
    return max(answer)


solution("100-200*300-500+20")