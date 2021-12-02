import sys
testcase = int(input())


for i in range(testcase):
    case = list(map(int,input().split()))
    count = 0
    avg = sum(case[1:])/case[0]
    
    for j in case[1:]:
        if j > avg:
            count += 1
    last = count / case[0] * 100
    print('%.3f'%last+"%")

        
    



