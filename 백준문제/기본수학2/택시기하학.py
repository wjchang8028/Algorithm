from math import pi #math의 pi임포트

r = int(input()) #반지름값 입력

a = r * r * pi #유클리드 기하학의 원넓이

b = r * r * 2

print(round(a,6))
print("%0.6f"%b)