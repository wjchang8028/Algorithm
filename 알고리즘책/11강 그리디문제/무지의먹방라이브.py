food_time = list(map(int,input().split()))

k = int(input())
print(food_time)
count = 0
for j in range(max(food_time)):
    for i in range(len(food_time)):

        if food_time[i] == 0:
            pass
        else:
            count += 1
            food_time[i] -= 1
        
        if count == k:
            print(count % i)
