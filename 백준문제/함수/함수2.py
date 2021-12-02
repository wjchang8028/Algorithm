list = []

for i in range(10000):
    i = str(i)

    num = 0
    for j in range(len(i)):
        num += int(i[j])
    d = int(i) + num

    list.append(d)

for i in range(10000):
    if i not in list:
        print(i)


