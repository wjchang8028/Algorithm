
def solution(array,m,start,end):
    
    while (start <= end):
        total = 0
        mid = (start + end) // 2 # 중간
        for i in array:
            if i > mid:
                total += i-mid

        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(result)
    return result

n,m = map(int,input().split())

array = list(map(int,input().split()))

solution(array,m,0,max(array))