cabinet = {3:"유재석", 100:"김태호"} #key:value

print(cabinet[3]) #키값을 빼오기
print(cabinet[100])
print(cabinet.get(3))


# print(cabinet[5]) 는 에러표시후 콘솔종료
print(cabinet.get(5)) #는 값이 없다고만 뜨고 콘솔계속 진행
print(cabinet.get(5,"사용가능한 키값"))

print(3 in cabinet) #키값 확인 boolean 형태
print(5 in cabinet)

cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새손님

print(cabinet)
cabinet["A-3"] = "김종국" #유재석이 이미사용중
cabinet["C-29"] = "조세호"
print(cabinet)

#집에간 손님
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

#key,value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)