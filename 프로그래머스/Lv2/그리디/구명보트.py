def solution(people, limit):
    answer = 0
    people.sort()
    
    i = 0
    j = len(people)-1
    count = 0
    while i <= j: # 중간부분까지
        count += 1
        if people[i]+people[j] <= limit:
            i += 1
        j -= 1
    print(count)
    
    return answer

solution([70,50,80,50,10,20,30,40] , 100)