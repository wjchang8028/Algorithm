# n = int(input())

# lst=[]
# maxi = []


# for i in range(n):
#     rope = int(input())
#     lst.append(rope)

# lst.sort()
# lst.reverse()

# # print(lst)

# for i in range(len(lst)):
#     maxi.append(lst[i] * (i+1))

# # print(maxi)
# print(max(maxi))

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    rope = [0] * 10001 # 로프가 버틸수있는 최대중량
    for _ in range(n): #입력받은 로프의 한계무게까지 반복
        rope[int(input())] += 1  #한계무게 부분 인덱스에 +1
    m, s = 0, 0
    for x in range(10000, -1, -1): 
        s += rope[x] #인덱스에 1이 있는 부분들을 전부 더해줌
        m = max(m, x * s) #인덱스값과 s값을 곱한값중 최대가 출력
    print(m)
main()