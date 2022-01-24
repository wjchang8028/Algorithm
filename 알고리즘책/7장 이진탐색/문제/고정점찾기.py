import bisect

def solution(array,start,end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == mid: #인덱스값과 해당 값이 같은지 확인하는 방법
        return mid
    elif array[mid] > mid:
        return solution(array,start,mid-1)
    elif array[mid] < mid:
        return solution(array,mid+1,end)

n = 5
array = [-15,-6,1,3,7]

index = solution(array,0,n-1)

if index == None:
    print(-1)
else:
    print(index)