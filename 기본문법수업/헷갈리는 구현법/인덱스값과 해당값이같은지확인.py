def IndexEqualValue(array):
    for i in range(len(array)):
        if array[i] == i:
            print(array[i])
    return

array = [1,1,3,3,2,5,4,3,1,5,2,3,4] # 인덱스와 같은값은 1, 3, 5 -> array[1] = 1 , array[3] = 3, array[5] = 5 
IndexEqualValue(array)