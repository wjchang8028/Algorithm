def solution(numbers):
    answer = 0

    for i in range(10):
        if i not in numbers:
            answer += i
    print(answer)

    return answer

numbers=[1,2,4,5,6,7,9,0] #3 8 없음

solution(numbers)