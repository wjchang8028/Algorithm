n = int(input()) #금액

#거슬러줄 동전 최소개수

# a = n // 500 #최대금액을 우선
# a1 = n - 500 * a
# b = a1 // 100
# b1 = a1 - b* 100
# c = b1 // 50
# c1 = b1 - 50* c
# d = c1 // 10
# d1 = c1 - d * 10 

# if d1 == 0:
#     print(a,b,c,d)
#     print(a+b+c+d)

coin_type = [500,100,50,10]

cnt = 0
for coin in coin_type:
    cnt += (n // coin) #해당 화폐로 거슬러 줄 수 있는 동전의 갯수 세기
    n %= coin # 동전을 거슬러 주고 남은 값

print(cnt)
