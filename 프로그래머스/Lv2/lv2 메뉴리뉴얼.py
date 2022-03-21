from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        print(candidates)

        sorted_candidates = Counter(candidates).most_common()
        print(sorted_candidates)
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    
    print(answer)
    return sorted(answer)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])