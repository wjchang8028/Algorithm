# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

n,m = map(int,input().split())
result = 0
for i in range(n):
    
    data = list(map(int,input().split()))

    #print(data) 
    
    min_value = min(data) #data리스트에서 가장 작은값

    result = max(result,min_value) # 그 작은값들중 가장 큰 값
print(result)

    
