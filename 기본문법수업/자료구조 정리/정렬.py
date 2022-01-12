#선택정렬


                #삽입 정렬 (이미 정렬되어있을 때 최선의 복잡도 O(n))
array = [7,5,9,0,3,1,6,2]

for i in range(1,len(array)): #2번째 인자부터 탐색하기 때문
    for j in range(i, 0 , -1): #정렬된 부분에서 뒤에서부터 크기비교 하면서 앞으로 넘어감
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1],array[j]
        else:
            break
print("선택",array)


                #퀵정렬 O(nlog(n))
array = [7,5,9,0,3,1,6,2]

def quick_sort(array,start,end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while (left <= right):
        while (left <= end and array[left] <= array[pivot]): #피벗보다 큰 데이터를 왼쪽에서부터 찾음
            left += 1

        while (right > start and array[right] >= array[pivot]): #피벗보다 작은 데이터를 오른쪽에서부터 찾음
            right -= 1

        if (left > start): #찾은 값이 엇갈리면 작은데이터와 피봇값과 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: #엇갈리는 부분이 없으면 작은데이터와 큰데이터 교체
            array[left], array[right] = array[right], array[left]

    quick_sort(array,start,right - 1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print("퀵",array)

                #pythonic quick sort
array = [7,5,9,0,3,1,6,2]
def quick_python(array):
    if len(array) <= 1:
        return array

    pivot = array[0] #맨앞이 항상 피벗
    tail = array[1:] #피벗을 제외한 배열

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_python(left_side) + [pivot] + quick_python(right_side)

print("파이썬퀵",quick_python(array))


                # 계수정렬(가장 작은 데이터부터 가장 큰데이터 까지 담길 리스트를 생성 후 정렬)
                # 최종적으로 리스트에 각 데이터가 몇번씩 등장했는지 카운트됨
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array)+1) # 가장 큰 수 만큼 배열생성

for i in range(len(array)):
    count[array[i]] += 1 #모든 숫자를 확인하면서 해당 인덱스에 1씩 추가(갯수 카운트)

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end = ',')

