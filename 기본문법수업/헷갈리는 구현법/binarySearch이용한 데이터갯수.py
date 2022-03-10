from bisect import bisect_left,bisect_right

def count_by_range(a,left_value,right_value): #리스트, 가장왼쪽값, 가장오른쪽값
    
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)

    return right_index-left_index

a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 갯수
print(count_by_range(a,4,4))

# -1에서 3까지의 데이터 갯수
print(count_by_range(a,-1,3))