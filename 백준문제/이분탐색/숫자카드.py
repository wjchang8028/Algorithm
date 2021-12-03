import sys

def binary(array,target,start,end):
    
    while start<=end:

        mid = (start+end) // 2
        
        if array[mid] == target:
            return array[start:end+1].count(target)

        elif array[mid] > target:
            
            end = mid - 1
        else:
        
            start = mid + 1
    return None

n = int(input())
nlist = sys.stdin.readline().split()
nlist.sort()

m = int(input())
mlist = sys.stdin.readline().split()


for i in mlist:
    result = binary(nlist,i,0,n-1)

    if result != None:
        print(result)
    else:
        print(0)