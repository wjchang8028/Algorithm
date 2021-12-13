n,m = map(int,input().split())

data = list(map(int,input().split()))

#1부터10까지 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    array[x] += 1 # [0,1,2,1,2,2,0,0,0,0,0]

result = 0

for i in range(1,m+1): #1번 인덱스의 수 * 남은무게마다의 수
    n-=array[i]
    result += array[i] * n
    # 무게1 : 1 * (2+1+2+2) = 7
    # 무게2 : 2 * (1+2+2) = 10
    # 무게3 : 1 * (2+2) = 4
    # 무게4 : 2 * (2) = 4

print(result)

#입력예제
# 8 5
# 1 5 4 3 2 4 5 2 답 25

