from sys import stdin
from collections import Counter

_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

Counterfunc = Counter(N) #n 리스트에서 count하는 함수
print(' '.join(f'{Counterfunc[m]}' if m in Counterfunc else '0' for m in M))
#m이 counterfunc에 있으면 f'{Counterfunc[m]}'를 join, 없으면 0, m이 돌때까지