#함수 간단히 가능
#이름없는함수라고도 불림

#(lambda 매개변수들 : 연산)(값,값)
def add(a,b):
    return a+b
print(add(3,7))

#add함수정의와 같은 형태의 lambda
print((lambda a,b: a+b)(3,7))
print((lambda a,b,c : a+b+c)(1,2,3))

a = [1,2,3]
b = [4,5,6]
print((lambda i,j : i+j)(a,b)) # [1,2,3,4,5,6]
print((lambda i,j: i+j , a,b)) # (<function <lambda> at 0x0000029DE2D2A170>, [1, 2, 3], [4, 5, 6])
print(list(map(lambda i,j : i+j , a,b))) #[5, 7, 9]

#람다표현식
array = [('홍길동',50),('이순신',32),('세종대',74)]
def my_key(x):
    return x[1]

print(sorted(array, key=my_key)) #[('이순신', 32), ('홍길동', 50), ('세종대', 74)]
print(sorted(array, key= lambda x: x[1])) #[('이순신', 32), ('홍길동', 50), ('세종대', 74)]