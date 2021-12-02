t = int(input()) #전체 테스트케이스
temp = []
temp2 = []           

for i in range(t):
    t2 = int(input()) #학교 수

    for j in range(t2):
        school, num = map(str,input().split())

        temp.append(school)
        temp2.append(int(num))

    a = max(temp2)

    find = temp2.index(a)

    print(temp[find])

    temp.clear()
    temp2.clear()

    

