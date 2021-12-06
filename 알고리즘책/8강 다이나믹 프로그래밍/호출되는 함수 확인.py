#재귀를 통한 피보나치수열 (탑다운)
d = [0] * 100 #탑다운 방식에서 사용되는 메모이제이션(임시 메모)

def fibo(x):
    print('f('+str(x)+')',end=" ")
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))


#반복문을 통한 피보나치수열 (바텀업)
d2 = [0] * 100 #바텀업 방식에서 사용되는 결과저장용 리스트(dp테이블)
d2[1] = 1
d2[2] = 1
n = 99

for i in range(3,n+1):
    d2[i] = d2[i-1] + d2[i-2]
print(d2[n])