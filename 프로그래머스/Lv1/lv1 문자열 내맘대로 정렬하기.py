def solution(strings, n):
    answer = []

    answer = sorted(sorted(strings),key=lambda x:x[n])
    print(answer)
    return answer


strings = ["abce", "abcd", "cdx","abcf"]
n = 2
solution(strings,n)