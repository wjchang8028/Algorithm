import sys

input = input()

list = list(map(str,input))
#print(list)
minus = 0
if '-' in list:
    minus = list.index('-')
    #print(minus)
    for i in range(minus+1,len(list)):
        if list[i] == '+':
            list[i] = '-'


new = ''.join(list)


print(eval(new))


