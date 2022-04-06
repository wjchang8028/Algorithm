#길이가 n인 벽을 2 * 1 과 1 * 2 타일로 채울때, 가짓수를 구하는 문제
import sys
sys.setrecursionlimit(10**6)

def solution(n):
    answer = 0
    d = [0] * 60001

    def memo(n):
        if n == 0 or n == 1:
            return 1
        
        if d[n] != 0:
            return d[n]

        d[n] = (memo(n-1) + memo(n-2)) % 1000000007
        
        return d[n]
    return memo(n)
print(solution(3))
print(solution(4))
print(solution(5))

def other_solution(n):
    a,b = 1,1

    for i in range(n):
        a, b = b, a+b
        print(a,b)
    print(a)
    return a % 1000000007

print(other_solution(7))
