#집합(set)
#중복안됨,순서없음

my_set = {1,2,3,3,3}
print(my_set)

#집합자료형의 연산
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])
print(a|b) #합집합 {1, 2, 3, 4, 5, 6, 7}
print(a&b) #교집합 {3, 4, 5}
print(a-b) #차집합 {1, 2}

#집합자료형 관련함수
data = set([1,2,3])

data.add(4) #데이터 추가 {1,2,3,4}
data.update([5,6]) #데이터 여러개추가 {1,2,3,4,5,6}
data.remove(3) #데이터 삭제 {1,2,4,5,6}


java={"유재석","김태호","양세형"}
python= set(["유재석","박명수"])

#교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

#차집합 (java 할 수 있지만 python 할 줄 모르는 개발자)
print(java - python)
print (java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java 하는법 까먹음
java.remove("김태호")
print(java)