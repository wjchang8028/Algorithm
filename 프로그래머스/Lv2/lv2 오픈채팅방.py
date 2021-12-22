def solution(record):
    answer = []
    temp = []
    array = []

    for i in range(len(record)):
        temp.append(list(record[i].split(" ")))
    
    # print(temp)

    for i in range(len(temp)):
        if temp[i][0] == 'Enter':
            array.append(['Enter',temp[i][1],temp[i][2]])

        
    # print(array) 

    for i in range(len(array)):
        if array[i][1] == array[len(array)-1][1]:
            array[i][2] = array[len(array)-1][2]
            
    # print(array)

    
    for i in range(len(temp)):
        if temp[i][0] == 'Change':
            for j in range(len(array)):
                if array[j][1] == temp[i][1]:
                    array[j][2] = temp[i][2]

    # print(array)

    for i in range(len(temp)):
        for j in range(len(array)):
            if temp[i][0] == array[j][0]:
                if temp[i][1] == array[j][1]:
                    
                    temp[i] = array[j]

    # print(temp)

    for i in range(len(temp)):
        if temp[i][0] == 'Enter':
            answer.append(temp[i][2]+"님이 들어왔습니다.")
        
        elif temp[i][0] == 'Leave':

            answer.append(array[0][2]+"님이 나갔습니다.")
        if temp[i][0] == 'Change':
            pass
    print(temp)
    print(array)
    print(answer)

    return answer

def solve(record):
    answer = []
    dic = {}

    for sentence in record:
        sentence_split = sentence.split()
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]

    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append(dic[sentence_split[1]]+"님이 들어왔습니다.")
        elif sentence_split[0] == 'Leave':
            answer.append(dic[sentence_split[1]]+"님이 나갔습니다.")
            
    print(sentence_split)
    print(dic)
    print(answer)
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solve(record)

# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]