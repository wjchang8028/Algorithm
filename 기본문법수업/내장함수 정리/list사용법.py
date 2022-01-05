#list에서 원소들 차례로 삭제.
array = [1,2,3,1,2,3,4]
delarr = [1,2,2]
#예상값 = [3,1,3,4]

#list에서 중복된 값 하나만 남기고 모두 제거
for i in delarr:
    if i in array:
        array.remove(i)
print(array)