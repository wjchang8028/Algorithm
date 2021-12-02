n = input()

x = ord(n[0])-96 # a = 97이기때문에 1,1로 맞춰줌
y = int(n[1]) #숫자값
count = 0

steps = [(-2,1),(-2,-1),(2,-1),(2,1),(-1,2),(-1,-2),(1,-2),(1,2)] #말이 이동할 수 있는 방법들의 수 

for i in range(len(steps)):
    mx = x + steps[i][0] #steps배열의 i번째 중 [0]번 인덱스값
    my = y + steps[i][1] #steps배열의 i번째 중 [0]번 인덱스값

    if mx >= 1 and mx <= 8 and my >=1 and my <= 8: #mx의 값이 범위 내 일때만 count + 1을 해줌
        count += 1
print(count)