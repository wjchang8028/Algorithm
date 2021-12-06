#리스트 []

#지하철 칸별로 10명,20명,30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [subway1,subway2,subway3]
print(subway)

subway = ["우재석","박명수","조세호"]
print(subway)

#조세호가 타고있는 칸
print(subway.index("조세호"),"번째 칸")

#하하가 다음 정류장에서 탐
subway.append("하하")
print(subway)

#정형돈이 유재석 과 조세호 사이에 탐
subway.insert(1,"정형돈") #insert(index,value)
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print("나간사람 : ",subway.pop())
print(subway)

print("나간사람 : ",subway.pop())
print(subway)

print("나간사람 : ",subway.pop())
print(subway)

#같은 이름의 사람이 몇명 있는지 확인
subway.append("우재석")
print(subway)
print(subway.count("우재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

#모두지우기
num_list.clear()
print(num_list)

#다양한 자료형과 함께 사용가능
mix_list=["조세호",20,True]
print(mix_list)

#리스트 확장
num_list=[1,4,5,2,3]
num_list.extend(mix_list)
print(num_list)