n = int(input())

temp = []

for i in range(n):
    a,b = input().split()
    temp.append((a,int(b)))

def setting(data):
    return data[1]

result = sorted(temp,key=setting)

for i in result:
    print(i[0],end= ' ')
    print(i[1],end= ' ')
