def solution(number, k):
    answer = ''
    stk = []
    for i in number:
        while stk and stk[-1] < i and k>0: #새로 들어온 원소가 기존값보다 크고, k가 0보다 클때 기존값을 pop시킴
            k-=1
            stk.pop()

        stk.append(i) 
        print(stk)

    return "".join(stk[:len(stk)-k])

solution("1231234",3)