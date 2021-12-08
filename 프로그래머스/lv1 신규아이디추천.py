import itertools

def solution(new_id):
    answer = ''
    temp = []

    new_id = new_id.lower() #1단계
    id = list(new_id)

    notallow = "~!@#$%^&*()=+[{]}:?,<>/"
    array = list(notallow)

    for i in id: #2단계
        if i not in notallow:
            temp.append(i)
    print(temp)

    g = itertools.groupby(temp) #3단계
    temp = [k for k, v in g]

    print(temp)

    if temp[0] == '.': #4단계
        temp.pop(0)
    elif temp[len(temp)-1] == '.':
        temp.pop(len(temp)-1)
    
    print(temp)

    if len(temp) == 0: #5단계
        temp.append('a')
    
    if len(temp) > 15:
        del temp[15:]

    print(temp)

    while len(temp) <= 2:
       temp += temp[-1]
        

    print(temp)

    print(answer)

    return answer

def solution_other(new_id):
    answer =''

    #1단계
    new_id = new_id.lower()

    #2단계
    for value in new_id:
        if value.islower() or value.isdigit() or value in ["-","_","."]:
            answer += value

    #3단계
    while '..' in answer:
        answer = answer.replace('..','.')
        print(answer)

    #4단계
    if answer[0] == '.':
        if len(answer) >= 2:
            answer = answer[1:]
        else:
            answer='.'
    if answer[-1] == '.':
        answer = answer[:-1]

    #5단계
    if answer =="":
        answer = "a"
    
    #6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    #7단계
    while len(answer) <3:
        answer += answer[-1]

    return answer

new_id = "abcdefghijklmn.p"

solution_other(new_id)