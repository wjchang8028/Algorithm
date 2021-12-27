
def solution(n): 
    if n <= 3: #124 순서
        return '124'[n-1]
    else:
        q,r = divmod(n-1,3)
        return solution(q) + '124'[r]


solution(4999999999)