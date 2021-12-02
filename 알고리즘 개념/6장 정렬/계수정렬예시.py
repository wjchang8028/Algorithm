array =[0,3,4,0,1,3,2,5,4,2,7,8,6,6]

#모든범위를 포함하는 리스트 선언 (모든값은 0으로 초기화)

count = [0] * (max(array)+1) #0부터 최대값+1만큼의 길이인 배열을 생성

for i in range(len(array)):
    count[array[i]] += 1 #각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end =' ')

