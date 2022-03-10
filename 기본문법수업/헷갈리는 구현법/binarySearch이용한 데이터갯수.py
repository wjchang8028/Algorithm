from bisect import bisect_left,bisect_right
# 기본적으로 정렬이 되어있는 상태에서 사용해야함

def count_by_range(a,left_value,right_value): #리스트, 왼쪽에서 찾을 값, 오른쪽에서 찾을 값

    right_index = bisect_right(a,right_value) # a 리스트에서 가장 오른쪽 + 1에 있는 인덱스값을 반환
    left_index = bisect_left(a,left_value) # a 리스트에서 가장 왼쪽에 있는 인덱스값을 반환

    print(left_index, right_index)

    return right_index-left_index

a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 갯수
print(count_by_range(a,4,4))

# -1에서 3까지의 데이터 갯수
print(count_by_range(a,-1,3))