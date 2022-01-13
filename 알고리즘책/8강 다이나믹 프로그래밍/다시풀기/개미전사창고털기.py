# 연속된 창고는 못털음
# 최대값 리턴

n = 6 #창고갯수
array = [1,3,1,5,17,9]

def solution(array,n):
    d = [0] * 101

    d[0] = array[0]
    d[1] = max(array[0], array[1])

    for i in range(2,n):
        d[i] = max(d[i-1],d[i-2]+array[i]) #amx(직전 창고까지의 총 식량, 두번째 전까지의 총 식량 + 현재창고의 식량)

    print(d[n-1])
    return d[n-1]

solution(array,n)