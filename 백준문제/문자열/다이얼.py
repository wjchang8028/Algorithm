word = input()


dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'] # 0,1,2,3,4,5,6,7
time = 0

for i in range(len(word)):
    for j in dial:
        if word[i] in j:
            time += dial.index(j)+3
print(time)

