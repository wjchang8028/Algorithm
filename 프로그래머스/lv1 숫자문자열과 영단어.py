def solution(s):
    answer = s

    num = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

    for i in num.items():
        answer = answer.replace(i[0],str(i[1])) #dictionary 사용. 키값으로 접근하고 그에 맞는 value값을 리턴할때 사용
    
    print(answer)
    return int(answer)

s = "2three445sixfivethreeseven"
#2 3 4 4 5 6 5 3 7
solution(s)