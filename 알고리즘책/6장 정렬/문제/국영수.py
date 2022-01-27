import sys
input = sys.stdin.readline
n = int(input())

name_list = []
kor_list = []
eng_list = []
math_list = []

for _ in range(n):
    name,k,e,m = input().split()
    name_list.append(name)
    kor_list.append(int(k))
    eng_list.append(int(e))
    math_list.append(int(m))

lst = list(zip(name_list,kor_list,eng_list,math_list))

lst.sort(key= lambda x: (-x[1],x[2],-x[3],x[0])) #국어 내림차순
for i in range(len(lst)):
    print(lst[i][0])