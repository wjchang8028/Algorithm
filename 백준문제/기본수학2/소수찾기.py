import sys
n = int(input())
num = map(int,sys.stdin.readline().split())
sosu = 0
for i in num: 

    error = 0

    if i>1:
        for j in range(2,i): #2부터 입력값까지 돌리기
            if i % j == 0:
                error += 1
        if error == 0:
            sosu += 1

print(sosu)
