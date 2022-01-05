#반복형태의 데이터 처리용

#순열 : 서로 다른 n개에서 서로다른 r개를 선택해 일렬로 나열 nPr = n * (n-1) * (n-2) * ... *(n-r+1)
    #P는 permutaion 의 약자
from itertools import permutations

data = ['a','b','c']
print(list(permutations(data,3))) # [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]



#조합 : 서로 다른 n개에서 순서관계없이 r개를 선택하는것 nCr = nCr = n * (n-1) * (n-2) * ... *(n-r+1) / r!
    #C는 combinations 의 약자
from itertools import combinations

print(list(combinations(data,2))) # [('a', 'b'), ('a', 'c'), ('b', 'c')]


#중복순열
from itertools import product
print(list(product(data,repeat = 2))) #2개를 뽑는 모든 순열 
#[('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]

from itertools import combinations_with_replacement
print(list(combinations_with_replacement(data,2))) #2개를 뽑는 모든 조합(중복허용)
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]






#Counter()