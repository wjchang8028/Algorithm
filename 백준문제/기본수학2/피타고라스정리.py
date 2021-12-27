def solution(b):
    answer = 0
    temp = []
   
    for i in range(1,b):
        c =  (i ** 2 + b ** 2 ) ** 0.5
        temp.append(c)
    print(temp)

    for i in temp:
        if i == int(i):
            answer = int(i)
            break
    
    if answer == 0:
        print(-1)
    else:
        print(answer)

    return answer

b = 12
solution(b)

# a<=b<=c <= 500000 이고 b만 매개변수로 줬을때 값 나오게하기. b = 12 -> c = 13 , b = 5 c = -1 , 