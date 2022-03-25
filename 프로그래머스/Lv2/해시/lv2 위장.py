from collections import defaultdict


def solution(clothes):
    hash_clothes = {}
    
    for value,key in clothes:
        # hash_clothes.setdefault(x[1],[]).append(x[0])
        hash_clothes[key] = hash_clothes.get(key,0) + 1
        print("get",hash_clothes.get(key,0) + 1)
    
    print(hash_clothes)

    answer = 1 
    for type in hash_clothes: 
        answer *= (hash_clothes[type] + 1) # 입지않는 경우의 수 1을 추가해줌 (옷1, 옷2, x) , (모1,x)

    print(answer-1) # 아무것도 안입는 경우는 빼주어야함

    return answer-1


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)

solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])
