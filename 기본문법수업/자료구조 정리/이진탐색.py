                # 이진탐색 (O(logN)) 단계별 탐색 범위를 반으로 계속 줄여나감

def binary_search(array,target,start,end):
    if start > end: #끝과 끝이 만나거나 엇갈리는순간부턴 끝
        return None

    mid = (start + end) // 2 # 중간값
    if array[mid] == target:
        return mid

    elif array[mid] > target: # 중간값이 찾고자하는값보다 클경우
        return binary_search(array,target,start,mid-1)

    else: # 중간값이 찾고자 하는 값보다 작은 경우
        return binary_search(array,target,mid+1,end)

array = [1,4,2,3,5,7,8,12]
target = 7
start = 0
end = len(array)
result = binary_search(array,target,start,end)
if result == None:
    print("원소없음")
else:
    print(array,target)
    print("찾는 숫자의 위치",result + 1)



                # 파라메트릭 서치 - 최적화 문제를 결정문제( 예, 아니오로 결정)로 바꾸어 해결하는 방법
                # ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화문제

