def solution(s):

    lst = list(s)
    pcount=0
    ycount = 0
   
    for i in lst:
        if ord(i) == 112 or ord(i) ==80:
            pcount += 1
        elif ord(i) == 121 or ord(i) == 89:
            ycount += 1
        else:
            pass
    
    if pcount == ycount:
        return True
    else:
        return False

def other_solution(s):
    a = s.lower().count('p') # 전부 소문자화 후 p의갯수 카운트
    b = s.lower().count('y') # y갯수 카운트
    print(a,b)

    if a == b:
        return True
    else:
        return False


s="pPoooyY"
solution(s)
other_solution(s)