python = "Python is Amazing"
print(python.lower()) #전부 소문자
print(python.upper()) #전부 대문자

print(python[0].isupper()) #맨앞이 대문자인가
print(len(python)) #총 길이
print(python.replace("Python","새로바꿈")) #리플레이스 함수

index = python.index("n") #index의 값을 정해줌
print(index)

index = python.index("n", index + 1) #그 전 index값 이후에 
print(index) 

print(python.find("java")) #원하는 값이 없을 경우 -1
#print(python.index("java")) 인덱스에서 값이 없을경우엔 콘솔에러

print(python.count("n")) #n이 몇번나오는지 세주는 함수