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

s="pPoooyY"
solution(s)