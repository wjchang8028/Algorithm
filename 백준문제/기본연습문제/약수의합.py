a = []
sum = 0
def solve(n):
    global sum
    for i in range(1,n-1):
        if n % i == 0:
            a.append(i)
            sum += i
    
while True:
    n = int(input())
    sum = 0

    if n == -1: #-1입력시 탈출
        break
    
    solve(n) 

    
    a = list(map(str,a))
    sik = ' + '.join(a)

    if sum == n:

        print(n,"=",sik)
    else:
        print(n,"is NOT perfect.")

    a.clear() #리스트 다시 비워주기



    

