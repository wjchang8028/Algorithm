def solution(w,h):
    answer = 1
    count = 0
    
    if w > h: #가로가 더 클때
        for i in range(w+2):
            if w // h  < i:
                count = i * h

                if count > w * h:
                    count -= 1
                break
    
    elif w < h: #세로가 더 클때
        for i in range(h+2):
            if h // w < i:
                count = i * w
                if count > w * h:
                    count -= 1
                break
           
    elif w == h: #정사각형일때
        count = w
    print(count)

    answer = w * h - count
    print(answer)
    return answer

import math
def other_solution(w,h):
    return w*h - (w+h - math.gcd(w,h)) #gcd는 최대공약수

solution(2,1)