#데이터의 갯수를 셀때 유용
from collections import Counter

word = "Hello World!"
c = Counter(word)
array = list(c.keys())
print(array) # ['H', 'e', 'l', 'o', ' ', 'W', 'r', 'd', '!'] #문법


arr = [1,1,1,2,2,2,2,5,5,4,4,4,4] 
c = Counter(arr) #리스트에서 중복된 값의 수를 세주기
a = list(c.keys()) #arr의 키값 (1,2,5,4)
print(a) # [1, 2, 5, 4]

b = list(c.values()) #arr의 키값에 묶여있는 값 카운트(3개,4개,2개,4개)
print(b) # [3, 4, 2, 4]

#Counter마크를 제거한 리스트(빈도수에따라서 자동정렬)
mostcounter = Counter(word).most_common() # 많은 순서대로 정렬.
print(mostcounter) # [('l', 3), ('o', 2), ('H', 1), ('e', 1), (' ', 1), ('W', 1), ('r', 1), ('d', 1), ('!', 1)]

#인자(2) 갯수 이상의 문자들만 출력
mostcounter = Counter(word).most_common(2)
print(mostcounter)
