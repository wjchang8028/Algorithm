#피보나치 함수를 재귀로 구현

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x-1) + fibo(x-2)

# print(fibo(30)) # 2의n승 시간복잡도. 비효율적

#피보나치 수열을 재귀적인 메모이제이션기법으로 구현

d = [0] * 100

#탑다운으로 구현
def fibo(x):
    #종료조건 (1혹은 2일때 1반환)
    if x == 1 or x == 2:
        return 1
    #이미 계산한 적이 있는 문제라면 그대로반환
    if d[x] != 0:
        return d[x]
    
    #아직 계산하지않은 문제라면 점화식에 따라서 피보나치 결과반환
    d[x] = fibo(x-1) + fibo(x-2)
    print(d[x])
    return d[x]

print(fibo(20))