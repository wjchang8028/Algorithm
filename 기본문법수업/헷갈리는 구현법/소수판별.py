def IsPrime(num):
    if num == 0 or num == 1: # 0과 1은 소수가 아님
        return False

    for i in range(2,num): # 2부터 자기 자신'이전'까지 나눠서 0이 되면 false
        if num % i == 0:
            return False

    return True # 그 외에는 전부 소수

print(IsPrime(17))
print(IsPrime(6))