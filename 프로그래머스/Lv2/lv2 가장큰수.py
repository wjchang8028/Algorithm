from itertools import permutations

def solution(numbers):
    temp = []
    a = list(permutations(numbers,len(numbers)))

    for i in range(len(a)):
        answer = ''
        for j in range(len(a[i])):
            answer += str(a[i][j])
        temp.append(answer)
    
    print(temp)
    print(max(temp))
    
    return max(temp)

# solution([3, 30, 34, 5, 9])

def solution2(numbers):
    lst = list(map(str,numbers))
    lst.sort(key = lambda x:x*3 , reverse = True)
    
    
    print("".join(lst))
    return str(int("".join(lst)))

solution2([3, 30, 34, 5, 9])