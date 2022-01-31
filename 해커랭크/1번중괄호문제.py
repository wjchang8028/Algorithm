#
def matchingBraces(braces):
    answer = []
    for i in range(len(braces)):
        stack = []

        for j in braces[i]:
            if len(braces[i]) % 2 == 0:
                if j =='{' or j =='[' or j == '(':
                    stack.append(j)
                elif j == '}':
                    if stack:
                        if stack[-1] == '{':
                            stack.pop()
                elif j == ']':
                    if stack:
                        if stack[-1] == '[':
                            stack.pop()
                elif j == ')':
                    if stack:
                        if stack[-1] == '(':
                            stack.pop()
            else:
                stack.append("-1")
        if len(stack) == 0:
            answer.append("YES")
        if len(stack) != 0:
            answer.append("NO")

    print(answer)
    return answer

braces = ['{}[]()', '{[}]}']
matchingBraces(braces)
