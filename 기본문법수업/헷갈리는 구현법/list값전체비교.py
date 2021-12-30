# 리스트에서 처음값과 뒤에있는 수들 비교할때.

array = [1,3,4,2,5]
temp = [6,7,8]
temp2 = []
for i in array:
    if temp: #if 리스트 : 은 값이 있을때만 돌고 없을땐 돌지않음
        print("temp내에 원소가 있을때",i)
    if temp2:
        print("empty",i)

        