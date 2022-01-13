n , m = 2 , 15
money = [2,3]

def solution(n,m,money):
    d = [1e9] * (m + 1) #나올 수 없는 값들로초기화
    d[0] = 0

    for value in range(n): #화폐단위
        for cost in range(money[value],m+1): # 값 
            if d[cost - money[value]] != 1e9: # 해당 인덱스 값 - 화폐딴위 값이 있으면 갱신
                d[cost] = min(d[cost],d[cost - money[value]]+1)

    if d[m] == 1e9: 
        print(-1)
    else:
        print(d) # [0, 1000000000.0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
        print(d[m])
    return

solution(n,m,money)