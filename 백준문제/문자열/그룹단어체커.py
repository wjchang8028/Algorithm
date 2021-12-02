import sys

case = int(input())
word = []

for i in range(case):
    word.append(input()) #입력받은 값을 리스트에 저장 ['happy', 'new', 'year']
    a = list(map(str,word[i]))
    # print(a) #a에 각각의 문자단위로 쪼개진 리스트 

    for j in range(len(a)):
        for k in range(j+2,len(a)):
            if a[j] == a[k]:
                break
        case = case - 1
            



print(case)


