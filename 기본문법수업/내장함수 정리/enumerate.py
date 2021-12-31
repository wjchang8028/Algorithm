# zip은 두개의 리스트를 한곳으로 묶어주는것. enumerate는 인덱스화 하는것

t = [1,3,5,7,9,11,13,15]

#enumerate를 쓰면 index 와 value로 묶은 튜플형태로 받을 수 있다. ex) a = 1 , b = 3 , c = 5 ... 순서정해놓을때
# 순서와 리스트의 값을 전달하는 역할 (enumerate = 열거하다)
for i in enumerate(t):
    print(i)


#시작 인덱스바꾸기(1부터시작)
for i,num in enumerate(t,start = 1):
    print(i,num)