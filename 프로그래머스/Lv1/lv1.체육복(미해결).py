def solution(n, lost, reserve):
    answer = 0

    array = [0] + [True] * (n)

    for i in range(len(lost)):
        array[lost[i]] = False
    
    print(array) #체육복이 없는 친구

    for i in range(len(reserve)):
       array[reserve[i]-1] = True 

    
    array[0] = 0
    answer = array.count(True)
    print(answer)
    
    return answer

lost = [3]
reserve = [1]
n = 3

solution(n,lost,reserve)