#데이터의 갯수를 셀때 유용함
from collections import Counter

word = "Hello World!"
c = Counter(word)
array = list(c.keys())
print(array)

#Counter마크를 제거한 리스트(빈도수에따라서 자동정렬)
mostcounter = Counter(word).most_common()
print(mostcounter)

for i in range(len(mostcounter)):
    print(mostcounter[i][0])

#인자(2) 갯수 이상의 문자들만 출력
mostcounter = Counter(word).most_common(2)
print(mostcounter)