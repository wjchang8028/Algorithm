print("a" + "b")
print("a","b")

#방법 1
print("나는 %d살입니다." %20) #d는 정수값을 의미함
print("나는 %s을 좋아합니다." %"파이썬") #s는 스트링값
print("Apple은 %c로 시작합니다" %"A") #c는 char

print("나는 %s색과 %s색을 좋아합니다" %("파란","빨간")) #두개가능


#방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아합니다" .format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아합니다" .format("검정","노랑"))
print("나는 {1}색과 {0}색을 좋아합니다" .format("검정","노랑"))


#방법 3
print("나는 {age}살이며, {color}색을 좋아합니다" .format(age=20,color="빨강"))

#방법 4
age = 20
color = "푸른"
print(f"나는 {age}살이며, {color}색을 좋아해요") #f를 써줘야 값이 나옴