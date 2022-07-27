#최대의 값을 만들기위해 오름차순정렬 후 해결

array = list(input())

array.sort() # 정렬

array = list(map(int,array))
total = 10

print(array)
while 0 in array: # array 안에 0이있으면 전부제거함
    array.remove(0)

for i in array:
    total *= i
print(total)


