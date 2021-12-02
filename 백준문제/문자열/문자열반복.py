import sys
case = int(input())

for i in range(case):
    input = sys.stdin.readline().split()
    word = list(map(str,input[1]))
    a = ""
    
    for j in range(len(word)):
        a += word[j]*int(input[0])
        
    print(a)

        
        
