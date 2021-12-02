n = int(input()) #사람수

min = list(map(int,input().split())) #p1~p5까지 인출하는데 걸리는 각각 시간

min.sort() #적은시간부터 정렬


wait = 0
total = 0

for i in range(len(min)):
    wait += min[i]
    total += wait

print(total)



