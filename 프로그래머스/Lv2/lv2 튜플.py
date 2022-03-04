import re
from typing import Counter
def solution(s):
    answer = []
    arr=[]
    for i in re.split('[{,}]',s):
        if i =="":
            pass
        else:
            arr.append(int(i))

    print(arr)

    c = Counter(arr).most_common()
    print(c)

    for i in c:
        answer.append(i[0])

    print(answer)

    return answer

s= "{{2},{2,1},{2,1,3},{2,1,3,4}}"
solution(s)

s = "{{20,111},{111}}"
solution(s)