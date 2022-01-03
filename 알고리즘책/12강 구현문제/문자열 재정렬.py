def solution(s):
    answer = ''
    temp =[]
    lst = []

    total = 0
    array = list(s)
    array.sort()

    for i in array:
        temp.append(ord(i))
    print(temp)
    
    for i in temp:
        if i < 65:
            total += int(chr(i))
        else:
            lst.append(chr(i))
        
    lst.append(str(total))
    answer = ''.join(lst)
    print(answer)
 
    return answer

s = 'K1KA5CB7'
s = 'AJKDLSI412K4JSJ9D'
solution(s)
