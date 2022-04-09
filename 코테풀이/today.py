from collections import Counter

def solution(call):
    temp = []
    lower_call = call.lower()
    # mostcounter = Counter(call).most_common()
    mostcounter = Counter(lower_call).most_common()
    print(mostcounter)
    max_value = mostcounter[0][1]
    print(max_value) #가장 많이 나온 값

    for i in range(len(mostcounter)):
        if mostcounter[i][1] == max_value:
            temp.append(mostcounter[i][0])
            temp.append(mostcounter[i][0].lower())
            temp.append(mostcounter[i][0].upper())
    print(temp)
    arr = list(call)

    imsi = [x for x in arr if x not in temp]
    answer = ''.join(imsi)
    print(answer)
    return answer

solution("abcabcdefabc")
solution("ABCabcA")
solution("AafAbbc")

