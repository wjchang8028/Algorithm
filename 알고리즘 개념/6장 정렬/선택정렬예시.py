array = [3,4,0,5,6,1,2,7 ]

for i in range(len(array)):
    min_index = i #가장 작은 인덱스

    for j in range(i+1, len(array)): #두번째부터 값 비교
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index],array[i] #스와프

print(array)


#스와프 예시
swap = [3,5]
swap[0],swap[1] = swap[1],swap[0]
print(swap)

#타언어는 temp = a , a = b, b = temp