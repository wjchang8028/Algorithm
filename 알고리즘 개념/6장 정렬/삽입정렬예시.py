array = [3,4,0,5,6,1,2,7 ]

for i in range(1,len(array)):
    for j in range(i,0,-1): #핀의 위치
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break
print(array)