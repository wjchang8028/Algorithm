#list에서 원소들 차례로 삭제.
array = [1,2,3,1,2,3,4]
delarr = [1,2,2]
#예상값 = [3,1,3,4]

#list에서 중복된 값 하나만 남기고 모두 제거
for i in delarr:
    if i in array:
        array.remove(i)
print(array)

#리스트 컴프리헨션
array = [i for i in range(10)] # 0~9까지 배열생성
print(array)

#1부터 9들의 수 중 제곱값
array = [i*i for i in range(1,10)]
print(array)

#2차원배열리스트 초기화
n = 3
m = 4
array = [[0] * n for _ in range(m)]
print(array)

#주의
array = [[0]*n] * m #참조값을 따서 같은 객체로 인식하기때문에 잘못된방법

#리스트 부가 함수
array = [1,2,3,4,5]
array.append(6)
array.insert(0,99) #insert(인덱스,넣을값)
print(array)

#리스트 
a = [1,2,3,4,5,5,5]
remove_set = {3,5} #집합 자료형 (dic)

#remove_list에 포함되지않은 값만 저장
result = [i for i in a if i not in remove_set]   
print(result)