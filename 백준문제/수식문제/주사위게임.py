t = int(input())

ascore = 100
bscore = 100

for i in range(t):
    a,b = map(int,input().split())

    if a > b: #a가 이긴경우
        bscore -= a #b점수에서 a수만큼 뺌
    elif a < b:
        ascore -= b
    elif a == b:
        pass

print(ascore)
print(bscore)