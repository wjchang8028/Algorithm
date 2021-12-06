zero = [1,0,1]
one = [0,1,1]

def fibo(x):
    length = len(zero)
    if length <= x:
        for i in range(length, x+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1]+one[i-2])
    print('{} {}'.format(zero[x],one[x]))
        


t = int(input())

for i in range(t):
    n = int(input())
    fibo(n)
    


    