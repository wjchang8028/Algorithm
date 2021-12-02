import sys

dosi = int(input())

distance = list(map(int,sys.stdin.readline().split()))

price = list(map(int,sys.stdin.readline().split()))

del price[len(price)-1]

oil = 0

totaldistance = sum(distance) #총 거리


temp = min(price)
index = price.index(temp)

#print(index)
if index != 0:
    for i in range(index): #도시갯수 최대 10만개

        oil += price[i] * distance[i]
        totaldistance -= distance[i]
    pin = len(price) - index

    oil += totaldistance * price[pin-1]
else:
    oil += totaldistance*price[0]
    
print(oil)






    
    






