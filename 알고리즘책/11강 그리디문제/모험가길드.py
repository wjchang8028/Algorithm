#최대의 값을 구하기때문에 내림차순으로 풀면 틀림
import sys

n = int(input())

array = list(map(int,sys.stdin.readline().split()))

# print(a) #모험가리스트 생성
array.sort(reverse=True)
count = 0
while array:
    if len(array) < 1:
        break
    
    count += 1
    
    del array[0:array[0]]
    print(array)

print(count)