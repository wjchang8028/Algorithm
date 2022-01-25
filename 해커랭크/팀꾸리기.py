from itertools import combinations

def countTeams(skills, minPlayers, minLevel, maxLevel):
    temp = []
    temp2 = []
    skills.sort()
    
    for i in skills:
        if minLevel <= i <= maxLevel:
            temp.append(i)


    for i in range(minPlayers, len(temp)+1):
        temp2.append(list(combinations(temp,i)))
    count = 0

    for i in range(len(temp2)):
        for j in range(len(temp2[i])):
            count += 1

    print(count)
    return

countTeams([12,4,6,13,5,10],3,4,10)