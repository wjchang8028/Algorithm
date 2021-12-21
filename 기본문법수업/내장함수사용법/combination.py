# 하나의 리스트에서 모든 조합을 계산을 해야 한다면, permutations, combinations을 사용
# 두개 이상의 리스트에서 모든 조합을 계산해야 한다면, product를 사용

from itertools import permutations
from itertools import combinations
from itertools import product

item = [1,2,3,4,5]
items = [[1,2,3],['a','b','c'],[4,5,6]]

#한개의 리스트에서 모든 내부 조합
print(list(permutations(item,2)))
print(list(combinations(item,2)))

#2개 이상 리스트조합
print(list(product(*items)))