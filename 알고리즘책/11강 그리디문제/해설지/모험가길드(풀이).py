#오름차순
#최대의 그룹수를 구해야하기 때문에 오름차순으로 풀어야함

n=int(input())

data = list(map(int,input().split()))
data.sort()

group = 0
count = 0

for i in data:
    count += 1 #인원수를 카운트
    if count >= i: #인원수가 공포도랑 같거나 높아지면
        group += 1 #그룹모집마감(+1)
        count = 0 #카운트 초기화
print(group)