def solution(nums):
    if len(nums)//2 > len(set(nums)):
        answer = len(set(nums))
    else:
        answer = len(nums) // 2
    print(answer)
    return answer

nums = [3,1,2,3]
solution(nums)