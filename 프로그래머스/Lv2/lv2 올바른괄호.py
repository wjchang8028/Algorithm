def solution(s):
    answer = True
    
    stack = []

    for i in s:
        if len(stack) == 0 and i == ')':
            stack.append(i)
            break
        elif i == ')':
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        answer = True
    else:
        answer = False
    print(answer)

    return answer

solution("()()")

solution("(())()")

solution("(()("	)

solution(")()(")

solution("()())")
