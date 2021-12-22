def solution(s):

    result = []
    if len(s) == 1:
        return 1
    for i in range(1,(len(s) // 2) + 1):
        b = ''
        cnt = 1
        temp = s[:i] #1부터 잘라내기

        for j in range(i,len(s),i): #자른 문자열의 크기만큼 증가하는 for문
            if temp == s[j:i+j]: #자른 문자열과 잘린부분부터 자른문자열의 길이만큼 또 자른부분이 같다면 ex) ab ab cd cd
                cnt += 1
            else:
                if cnt != 1:
                    b = b + str(cnt) + temp #abab -> 2ab
                else:
                    b = b + temp #ababc -> 2abc
                temp = s[j:j+i]
                cnt = 1
        if cnt != 1:
            b = b + str(cnt) + temp
        else:
            b = b + temp

        result.append(len(b))
        answer = min(result)
    print(result)
    print(answer)
    return answer

s = "aabbaccc"

solution(s)