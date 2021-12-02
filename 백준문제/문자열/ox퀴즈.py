import sys
testcase = int(input())

for i in range(testcase):
    count = 0;
    score = 0;
    ox = sys.stdin.readline()
    for j in range(len(ox)-1):
        if ox[j] == 'O':
            count += 1
            score +=count 
        elif ox[j] =='X':
            count = 0
    print(score)

        
