# def solution(n):
#     answer = 0
#     temp = []
#     array = []
#     a = int(n ** (1/3))
#     for i in range(a,-1,-1):
#         if a == 1:
#             temp.append(1)
#         temp.append(3**i)

#     print(temp)
#     for i in temp:
#         cnt = 0
#         cnt += n // i
#         array.append(cnt)
#         n %= i

#     array.reverse() #3진법 뒤집기
#     print(array) 

#     for i in range(len(array)):
#         answer += array[len(array)-1-i] * 3 ** i
#     print(answer)
#     return answer

def solution(n):
    answer = ''

    while n >= 1:
        n, rest = divmod(n, 3)
        answer += str(rest)
        print(answer)

    answer = int(answer, 3) #int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌
    print(answer)
    return answer
n = 45
solution(n)