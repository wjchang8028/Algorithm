dic = {"]": "[", ")": "(", "}": "{"}


def solution(s):
    answer = 0

    cnt = 0
    while cnt != len(s):
        stack = []
        s = s[1:len(s)] + s[0] #리스트 회전
        print(s)
        answer_s = True

        for c in s:
            if c == "[" or c == "(" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    answer_s = False
                    break
                if dic[c] == stack[len(stack) - 1]:
                    print("c",c,"dic[c]:",dic[c])
                    stack.pop()
                else:
                    answer_s = False
                    break

        if len(stack) != 0:
            answer_s = False

        if answer_s == True:
            answer += 1

        cnt += 1
    print(answer)
    return answer


solution("[](){}")

solution("[)(]")