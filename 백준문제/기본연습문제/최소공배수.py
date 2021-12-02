t = int(input())

def choiso(a,b):
    if b == 0:
        return a #두 수의 최대공약수
    else:
        return choiso(b,a%b)

for i in range(t):
    a,b = map(int,input().split())

    choidea = choiso(a,b)

    print(a*b//choidea)

