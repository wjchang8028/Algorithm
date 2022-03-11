from collections import deque

def solution(H):
    answer = [[]]
    while True:
        rec = H
        n = rec.pop(0)

        print("n",n)

        if n == 0:
            break
        stack =deque()
        answer = 0

        for i in range(n):
            while len(stack) != 0 and rec[stack[-1]] > rec[i]:

                print(stack)
                temp = stack.pop()
                print(temp)
                print(stack)

                if len(stack) == 0:
                    width = i
                    print("width",width)
                else:
                    width = i -stack[i] -1
                    print("width",width)
                answer = max(answer,width * rec[temp])
            stack.append(i)
        
        print("stack",stack)

        while len(stack) != 0:
            cnt = 1
            temp = stack.pop()
            # print(temp)
            if len(stack) == 0:
                width = n
            else:
                width = n - stack[-1] -1

            if width * rec[temp] >= answer:
                cnt += 1
            answer = max(answer,width * rec[temp])
        print(cnt)
        print("answer",answer)
        return answer
    
solution([2,2,1,1,3])



