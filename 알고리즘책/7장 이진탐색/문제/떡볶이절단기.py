
m,n = map(int,input().split()) #떡의 갯수, 요청길이

array = list(map(int,input().split()))

print(array) #떡길이 리스트

start = 0
end = max(array)

result = 0
while (start <= end):
    mid = (start+end) // 2

    total = 0
    
    for  i in array: #떡볶이들이 mid보다 클때 잘라낸 총길이
        if i > mid:
            total += i - mid

    if total < n: #잘라낸 떡볶이들 길이의 합이 원하는 길이보다 작을때
        end = mid - 1  #더 크게 잘라야하므로 mid를 낮추기
    else: #길이의 합이 원하는길이보다 크거나 같을때
        result = mid 
        start = mid + 1 #중간값보다 큰값들만 찾아내면 됨
print(result)

