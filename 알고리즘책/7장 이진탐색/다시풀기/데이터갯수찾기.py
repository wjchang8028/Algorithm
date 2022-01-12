from bisect import bisect_left,bisect_right

def solution(array,target):
    answer = 0
    right = bisect_right(array,target)
    left = bisect_left(array,target)
  
    if right >= len(array):
        answer = -1
    else:
        answer = right - left

    print(answer)
    
    return answer

n = 7
target = 2

array = [1,1,2,2,2,2,3] # 2는 4개
solution(array,target)