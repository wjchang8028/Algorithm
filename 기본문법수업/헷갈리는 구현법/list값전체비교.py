# 리스트에서 처음값과 뒤에있는 수들 비교할때.

array = [1,3,4,2,5]
temp = []
for i in range(len(array)):
    if array[0] < array[i]:
        print(array[i])
        