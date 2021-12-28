#두그룹의 데이터를 서로 묶어주는 파이썬 내장함수

numbers = [1,2,3]
letters = ["A","B","C"]

#인덱스없이
for pair in zip(numbers,letters):
    print(pair)

#인덱스있게
for i in range(3):
    pair = (numbers[i],letters[i])
    print(pair)

#리스트에 있는 zip을 그룹별로 unpacking
pairs = list(zip(numbers,letters)) #zip을 리스트에 담기
numbers,letters =zip(*pairs) #언패킹
print(numbers)
print(letters)


#병렬처리 (여러그룹의 인자들이 차례로 출력)
for number,lower,upper in zip("12345","abcde","ABCDE"):
    print(number,lower,upper)



#dictionary화 (두개 리스트) *주의사항 : 리스트의 인자가 다를땐 가장짧은 인자기준으로 데이터가 엮이고 나머진 버려짐
keys = [1,2,3]
values = ['a','b','c']
dic = dict(zip(keys,values))
print(dic)
