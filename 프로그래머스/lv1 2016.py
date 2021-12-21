#윤년은 366일
def solution(a, b):
    answer = ''
    day = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    total = 0
    for i in range(a):
        total += day[i]
    total += b
    if total % 7 == 1:
        answer = "FRI"
    elif total % 7 == 2:
       answer = "SAT"
    elif total % 7 == 3:
        answer = "SUN"
    elif total % 7 == 4:
        answer = "MON"
    elif total % 7 == 5:
        answer = "TUE"
    elif total % 7 == 6:
        answer = "WED"
    else:
        answer = "THU"
    
    print(answer)

    return answer

a=1
b=1
solution(a,b)