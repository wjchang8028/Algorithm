def solution(tstring, variables):
    answer = ''
    dict = {}

    for i in range(len(variables)):
        dict[variables[i][0]] = variables[i][1]
    arr2= list(tstring.split())
    arr = list(tstring.split())
    max_roof = 1000
    roof_value = 0

    while True:
        roof_value += 1
        for i in range(len(arr)):
            if arr[i][0] == '{' and arr[i][-1] == '}':
                if arr[i][1:-1] in dict:
                    arr[i] = dict[arr[i][1:-1]]

        answer = ' '.join(arr)

        if '{' not in answer:
            break
        if roof_value == max_roof:
            temp = list(answer.split())
            for i in range(len(temp)):
                if temp[i][0] == '{' and temp[i][-1] == '}':
                    if temp[i][1:-1] in dict:
                        temp[i] = arr2[i]
            answer = ' '.join(temp)
            break

    print(answer)
    return answer



    

solution("this is {template} {template} is {state}" , [["template", "string"], ["state","changed"]])
solution("this is {template} {template} is {state}",[["template", "string"], ["state", "{template}"]])
solution("{a} {b} {c} {d} {i}",[["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]])