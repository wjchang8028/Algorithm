from collections import Counter

def solution(participant, completion):
    answer = ''
    pcounter = Counter(participant)
    ccounter = Counter(completion)

    answer = pcounter - ccounter

    return list(answer.keys())[0]

participant = ["leo", "kiki", "eden","eden"]	
completion = ["eden", "kiki","leo"]

print(solution(participant,completion))