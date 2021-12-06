n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): #1시 23분 42초 이면 [1,2,3,4,2]내에 3이 있는지 확인
                count += 1

print(count)

