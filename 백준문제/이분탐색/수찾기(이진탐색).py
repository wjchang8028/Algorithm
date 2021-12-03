def binary(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1
    return None

n = int(input())
nlist = list(map(int,input().split()))

m = int(input())
mlist = list(map(int,input().split()))

nlist.sort()

for i in mlist:
    result = binary(nlist,i,0,n-1)
    if result != None:
        print(1)
    else:
        print(0)