array = list(map(int,input()))

one = 0
zero = 0

if array[0] == 1:
    one += 1
elif array[0] == 0:
    zero += 1

for i in range(1,len(array)):
    if array[i-1] != array[i]: #이전값과 현재값 비교시 다르다면
        if array[i] == 1: #현재값이 1이면 zero카운트에 +1
            zero += 1
        else:   #현재값이 1이 아니면 one 카운트에 +1
            one += 1
    

print(min(zero,one))


        

