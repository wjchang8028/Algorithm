from itertools import product


def solution(word):
    answer = 0
    dict = []

    for i in range(1,6) :
        dict += list(map(''.join, product("AEIOU", repeat = i)))
    dict.sort() 

    answer = dict.index(word) + 1
    print(answer)

    return answer

solution("AAAAE")

