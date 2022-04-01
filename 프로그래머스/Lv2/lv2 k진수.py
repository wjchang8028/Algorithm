import re


def deciToBin(num, n): # 10진수에서 n 진수로
    rev_base = ''

    while num > 0:
        num, mod = divmod(num, n)
        rev_base += str(mod)
    return rev_base[::-1] 

def IsPrime(num):
    if num == 0 or num == 1: # 0과 1은 소수가 아님
        return 0

    for i in range(2,int(num ** 0.5) + 1): 
        if num % i == 0:
            return 0

    return 1 # 그 외에는 전부 소수

def solution(n, k):
    answer = 0
    
    transited = deciToBin(n, k) # 진법변환
    transited = re.sub('0+', '0', transited) # 정규식 표현법
    if transited[0] == '0':
        transited = transited[1:]
    if transited[-1] == '0':
        transited = transited[:-1]
    nums = list(map(int, transited.split('0')))

    print(nums)

    for i in nums:
        answer += IsPrime(int(i))

    print(answer)
    return answer

solution(437674,3)
solution(110011,10)
solution(524287, 2)