def solution(n, arr1, arr2):
    answer = []
    pan = []

    for i in range(len(arr1)):
        pan.append(list(bin(arr1[i] | arr2[i])[2:].zfill(n)))
    # print(pan)

    for i in range(len(pan)):
        for j in range(len(pan[i])):
            if pan[i][j] == '1':
                pan[i][j] = '#'
            else:
                pan[i][j] = ' '
    
    # print(pan)

    for i in range(len(pan)):
        str = ''.join(pan[i])
        answer.append(str)
    print(answer)
    return answer

def other_solution(n,arr1,arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a = str(bin(i|j)[2:])
        
        a = a.rjust(n,'0')
        # print(a)

        a = a.replace('1','#')
        a = a.replace('0',' ')
        print(a)

        answer.append(a)
    print(answer)
    return answer

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
# solution(n,arr1,arr2)
other_solution(n,arr1,arr2)