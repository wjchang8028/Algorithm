from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)

    queue.append([numbers[0],0]) # 비어있는 큐에 양수 음수 두가지 경우를 저장
    queue.append([-1 * numbers[0] , 0])

    print(queue)

    while queue:
        value,idx =queue.popleft()
        idx += 1 #인덱스를 1씩 더해주기

        if idx < n :
            queue.append([value + numbers[idx], idx]) # 양수를 더해주는 경우
            queue.append([value - numbers[idx], idx]) # 음수를 더해주는 경우
        else:
            if value == target: # 조합한 값이 target값과 같다면
                answer += 1
    print(answer)
    return answer

solution([1,1,1,1,1], 3) # 1, -1로 3을 만들 수 있는 경우의 수 

solution([4,1,2,1], 4) # 양수 음수로 4를 만들 수 있는 경우의 수

answer2 = 0
def DFS(idx,numbers,target,value):
    global answer2
    n = len(numbers)

    if idx == n and target == value:
        answer2 += 1
        return 
    if idx == n:
        return 
    
    DFS(idx + 1,numbers,target,value + numbers[idx])
    DFS(idx + 1,numbers,target,value - numbers[idx])

def other_solution(numbers,target):
    global answer2
    DFS(0,numbers,target,0)
    print(answer2)
    return answer2

other_solution([1,1,1,1,1],3)


# 각 수의 음 양수로 만들 수 있는 값들 중 target값이 되는 경우의 수
my_answer = 0

def my_dfs(index,numbers,target,value):
    global my_answer

    n = len(numbers)

    if index == n and target == value: # 범위 설정 그리고 찾고자 하는 값이 나오면
        my_answer += 1
        return 
    
    if index == n: # 찾고자 하는 값이 안나와도 리턴
        return 

    my_dfs(index + 1,numbers,target, value + numbers[index]) # 양수 
    my_dfs(index + 1,numbers,target, value - numbers[index]) # 음수

def my_solution(numbers, target):
    global my_answer
    my_dfs(0,numbers,target,0)

    print(my_answer)    
    return 

my_solution([1,1,1,1,1],3)