n , m = 4,6 # 떡갯수, 원하는 떡길이
array = [19,15,10,17]

def wrong_solution(array,m,start,end): #잘못된 풀이
    answer = 0
    if start > end:
        return None

    mid = max(array) // 2
    # print(mid) 떡의 가운데 
    total = 0
    for i in array:
        if i >= mid:
            if i - mid > 0:
                total += i - mid

    if total > m:
        return solution(array,m,mid+1,end)
    elif total < m:
        return solution(array,m,start,mid-1)
    else:
        print(mid)
        return mid

def correct_solution(array,m,start,end):
    while (start <= end):
        total = 0
        mid = (start + end) // 2 # 떡의 중간점

        for x in array:
            if x > mid:
                total += x - mid

        if total < m : # 떡의 총길이가 원하는 값보다 작으면
            end = mid - 1 # 더 짧게 잘라야지
        else: # 원하는 값보다 크게 나오거나 같게나오면
            result = mid # 값을 저장해주고 
            start = mid + 1 # 더 크게 짤라야지

    print(result)
    return result

correct_solution(array,m,0,max(array))