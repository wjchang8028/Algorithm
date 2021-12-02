coin_value = [] #동전종류 리스트

n,k = map(int,input().split())

for i in range(n):
    value = int(input()) #동전종류 입력
    coin_value.append(value)

coin_value.reverse()
# print(coin_value) #동전종류 리스트에 값 들어온것 확인


count = 0 #동전의총 갯수

for coin in coin_value:
    
    count += k // coin # 전체값에서 해당코인값을 큰순서부터 나눠준 몫을 카운트

    k = k % coin #동전값을 나눈 나머지

print(count)