n = int(input())


coin = list(map(int,input().split()))

price = 1 #금액의 최솟값
coin.sort()

for i in coin: #price가 i까지의 금액을 만들수있다는 공식 i까지는 다 만들수있음
    if price < i:
        break
    price += i  

print(price)
