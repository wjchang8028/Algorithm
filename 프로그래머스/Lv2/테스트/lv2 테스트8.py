def solution(numbers):
    answer = []

    for i in numbers:

        if i % 2 == 0:
            answer.append(int(i+1))
            
        else:
            a = '0'+bin(i)[2:]
            index = a.rfind('0')

            a = list(a)
            a[index] = '1'
            a[index+1] = '0'
            b = int(''.join(a),2)

            answer.append(int(b))

    print(answer)
    return answer

solution([2,7,15])

