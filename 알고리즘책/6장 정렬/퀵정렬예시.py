array = [3,4,0,5,6,1,2,7]

def quick_sort(array,start,end):
    if start >= end: #원소가 1개인경우 분할이 불가하므로 종료
        return
    pivot = start # 피벗은 첫번째 원소

    left = start + 1
    right = end

    while left <= right:
        #피벗보다 큰 데이터를 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right : #엇갈렸다면 작은데이터와 pivot 교환
            array[right],array[pivot] = array[pivot],array[right]
        else: #엇갈리지않았다면 작은데이터와 큰데이터 교환
            array[left], array[right] = array[right],array[left]
    #분할 이후 왼쪽부분과 오른쪽부분에서 각각 정렬 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)