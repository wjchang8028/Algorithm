def solution(s): # 중간부터 값이 있으면 오류
    answer = 0
    for i in range(1,len(s)+1):
        reverse_pelin = ''
        pelindrome = s[:i]
        for j in range(len(pelindrome)-1,-1,-1):
            reverse_pelin += pelindrome[j]
        
        if pelindrome == reverse_pelin:
            answer = len(pelindrome)

    print(answer)
    return answer

solution("abcdcba")
solution("abacde")
solution("abbbc") # 정답 3, 오답 1
solution("abbba")

def perlindrome(temp):
    if temp == temp[::-1]:
        return True
def other_solution(s):
    max_value = 0

    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if perlindrome(s[i:j]):
                if max_value < len(s[i:j]):
                    max_value = len(s[i:j])
    print(max_value)
    return max_value

other_solution("abcdcba")
other_solution("abacde")
other_solution("abbbc")
