from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    for i in info:
        conditions = i.split()[:4]
        score = int(i.split()[-1])
        for r in range(5):
            combi = list(combinations(range(4),r))

            for c in combi:
                test_cases = conditions[:]
                for v in c:
                    test_cases[v] = '-'
                info_dict['_'.join(test_cases)].append(score)

    for item in info_dict:
        info_dict[item].sort()

    for q in query:
        q = q.replace('and','').split()
        conditions = '_'.join(q[:-1])
        score = int(q[-1])

        # print(conditions,score)

        if conditions in list(info_dict):
            data = info_dict[conditions]
            print(data)
            if len(data) > 0 :
                start,end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= score:
                        end = (start + end) // 2 
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)
        else:
            answer.append(0)
    print(answer)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])