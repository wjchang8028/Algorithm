#이진 탐색 소스 구현(재귀)
def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end)  // 2

    #찾은경우 중간점 index반환
    if array[mid] == target:
        return mid

    #중간점의 값보다 찾고자하는 값이 적은 경우 확인
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    
    #중간점의 값보다 찾고자하는 값이 큰경우 확인
    else:
        return binary_search(array,target,mid+1,end)

#n(원소의 갯수)과 target(찾고자하는 문자열)을 입력
n,target = list(map(int,input().split()))

array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)

if result == None:
    print('원소존재하지않습니다')
else:
    print(result+1)


# 10 7
# 1 2 3 4 5 6 7 8 9 10