import math
def solution(arr):
    
    def cal(a,b):
        t = (a // math.gcd(a,b)) * (b // math.gcd(a,b)) * math.gcd(a,b)
       
        return t
        
    
    answer = 0
    for i in range(1,len(arr)):
        arr[i] = cal(arr[i-1],arr[i])
        answer = arr[i]
    print(answer)
    return answer

solution([2,6,8,14])