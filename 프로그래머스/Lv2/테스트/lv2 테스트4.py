
def solution(msg):
    answer = []
    dic = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(1,27)))
    count = 27
    i = 0
    search = ""

    while i < len(msg):
        search += msg[i]
        print(search)
        if search in dic:
            i+=1   
            continue
        else:
            dic[search] = count
            count += 1
            s = search[:-1]
            answer.append(dic[s])
            search=''
    
    answer.append(dic[search])
    print(answer)
    return answer

# solution("KAKAO")

def other_solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    print(d)
    answer = []

    while True:

        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            print(msg[0:i], answer)
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]]) # 1. msg[0:2] = KA
                d[msg[0:i]] = len(d)+1 # 1.d[msg[0:2]] = len(d) + 1
                msg = msg[i-1:] # 1.msg[1:]
                break

    return answer

other_solution("KAKAO")
