def solution(s):
    answer = ''
    lst = []
    
    arr = s.split(" ")

    for i in range(len(arr)):
        word = ''
        for j in range(len(arr[i])):
            if j == 0 :
                temp = arr[i][j].replace(arr[i][j],arr[i][j].upper())
                word+= temp
            else:
                temp = arr[i][j].replace(arr[i][j],arr[i][j].lower())

                word+= temp
        lst.append(word)
    
    print(lst)

    for i in range(len(lst)):
        answer += lst[i]

        if i != len(lst) - 1:
            answer += " "
    
    print(answer)
    return answer

solution("3people unFollowed me")
solution("for the last week")