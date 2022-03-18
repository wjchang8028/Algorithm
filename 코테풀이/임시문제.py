from collections import deque
from concurrent.futures import process


def solution(n):
    temp = []
    for i in range(1,100001):
        if i // n == i % n :
            temp.append(i)
    print(sum(temp))


# solution(2)
# solution(3)

def other_solution(n):
    answer = 0
    for i in range(1,n):
        a = n*i + i
        answer += a

# other_solution(2)
# other_solution(3)

def second(data):
    queue = deque()
    processing_time = -1
    result = []
    working = []
    waiting = []
    max_time = max(data)[1] + max(data)[2]
    print(max_time)

    for time in range(max_time):
        processing_time += 1
        for i in data:
            if time == i[1] and len(working) == 0 :
                working.append(i[0])

            elif time == i[1]:
                waiting.append(i[0])
        
        if time == data[0][2]:
            if len(working) != 0:
                working.pop()
            else:
                pass

            
            
           
        print(time,"시 ", "work: ",working ,"wait: ", waiting)



    return result

second([[1,0,5],[2,2,2],[3,3,1],[4,4,1],[5,10,2]])

def third(grid):
    answer = 0
    imsi = []
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            imsi.append(grid[i][j])
    number_list = list(set(imsi))

    print(number_list) 

    width = 0

    for x in range(len(grid)):
        for y in range(len(grid)):
            for num in number_list:
                if grid[x][y] == num:
                    width += 1
                
                if grid[x][y] != num:
                    pass


            print(width)
            for i in range(width):
                if 0<= x - i < len(grid) and 0 <= y+i < len(grid):
                    if grid[x-i][y+i] == num:
                        answer += 1 

            
    print(answer)
    return answer

# third([[2,1,1,3,5,1],[1,1,3,3,5,5],[8,3,3,3,1,5],[3,3,3,4,4,4],[3,3,4,4,4,4],[1,4,4,4,4,4]])
# third([[0,1,1],[1,1,0]])
