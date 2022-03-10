def IsPrime(num):
    if num == 0 or num == 1: # 0과 1은 소수가 아님
        return False

    for i in range(2,num): # 2부터 자기 자신'이전'까지 나눠서 0이 되면 false
        if num % i == 0:
            return False

    return True # 그 외에는 전부 소수

print(IsPrime(17)) # True
print(IsPrime(6)) # False

def eratostenes(n): # 에라토스테네스의 체(시간효율성 업)
    answer = 0
    temp = []
    sosu = [False,False]+[True] * (n-1)

    for i in range(2,n+1):
        if sosu[i]:
            temp.append(i)
            for j in range(2*i,n+1,i):
                sosu[j] = False
    print(sosu)
    return answer

eratostenes(17)
# [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True]