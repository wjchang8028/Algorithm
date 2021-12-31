#조건문에 수식없이 list 만 받을때.

array = [1,3,4,2,5]
temp = [6,7,8]
temp2 = []
for i in array:
    if temp: #if 리스트 : 은 값이 있을때만 돌고 없을땐 돌지않음
        print("temp내에 원소가 있을때",i)
    if temp2:
        print("empty",i)


#스택이나 큐 다룰  때 많이 사용
from collections import deque
stack = [1,2,3,4,5,6,7,8,9,10] #기본 리스트는 스택형태
deque = deque(stack) # 스택을 큐형태로 만듬.

while deque: #deque 가 없을때까지
    deque.popleft() # 선입선출
    print(deque)

while stack: #stack 이 없을때까지
    stack.pop() #선입후출
    print(stack)