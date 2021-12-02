import sys
ischeck = 0
word = list(map(str,sys.stdin.readline().strip())) #.strip은 개행문자 제거 (\n)
imsi = []
for i in range(len(word)):
    imsi.append(word[len(word)-1-i])


for i in range(len(imsi)):
    if imsi[i] != word[i]:
        ischeck = 0
        break
    else:
        ischeck = 1

print(ischeck)


