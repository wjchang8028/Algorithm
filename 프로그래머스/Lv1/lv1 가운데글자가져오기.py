def solution(s):
    answer = ''
    if len(s) % 2 == 0: #짝수면
        answer = s[(len(s)-1)//2:len(s)//2 + 1]
    else:
        answer = ''.join(s[(len(s)-1)//2])
    print(answer)
    
    return answer

solution('abcd')