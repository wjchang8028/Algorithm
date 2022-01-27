array = [['홍길동',1,3,5],['장보고',2,2,6],['둘리',1,3,7],['또치',1,3,2],['나단',1,3,7]]

array.sort(key=lambda x:(-x[1],x[2],x[3],x[0])) # [1] 내림차순. [1]이 같을경우 [2]로 오름차순, [1][2]가 같을경우 [3]으로 오름차순 , [1][2][3] 모두 같으면 [0]으로 오름차순

print(array)
# [['장보고', 2, 2, 6], ['또치', 1, 3, 2], ['홍길동', 1, 3, 5], ['나단', 1, 3, 7], ['둘리', 1, 3, 7]]