def solution(array1,array2,k):
    answer = 0
    array1.sort()
    array2.sort(reverse=True)

    print(array1,array2)
    
    for i in range(k):
        if array1[i] < array2[i]: #중요! 2번 배열값이 1번보다 작으면 바꿀 필요없음
            array1[i],array2[i] = array2[i],array1[i]
        else:
            break

    print(array1,array2)

    print(sum(array1))
    return sum(array1)

n,k=5,3
array1 = [1,2,5,4,3]
array2 = [5,5,6,6,5]
solution(array1,array2,k)