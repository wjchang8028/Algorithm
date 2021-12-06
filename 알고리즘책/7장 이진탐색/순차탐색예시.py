# 3 나동빈
# 나동빈 김철수 최유리


def sequential_search(n,target,array):
    for i in range(n):
        if array[i] == target:
            return i + 1

num,name = map(str,input().split()) #사람수,찾을사람

human = list(map(str,input().split()))

print(human)
print(sequential_search(int(num),name,human))