#실수형
print(5)
print(-10)
print(3.14)
print(2*5)
print(3*(1+2))

#문자열
print('풍선')
print('나비')
print('나비'*5)

#불린
print(5>10)
print(True)
print(not False)
print(not(5>10))

# 문장

animal = "햄스터";
name = "해피";
age = 2;
hobby = "공굴리기";
is_adult = age >=3;

'''
주석 다 됩니다
'''
print("우리집" + animal + "는 이름이 "+name+"입니다")
print(name + "이는 "+str(age)+"살이며, "+ hobby +"을 아주 좋아해요")
print(name,  "이는 ",age,"살이며, ", hobby ,"을 아주 좋아해요") #컴마를 쓰면 str로 묶어주지않아도됨
print(name+"이는 어른일까요? "+ str(is_adult))

#퀴즈

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")