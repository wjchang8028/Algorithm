#스택의 초기화
stack = [1,2,3]

#스택의 추가
stack.append(4)
print("추가 : " , stack)

#스택의 삭제 (맨 뒤부터 빠짐)
top = stack.pop()
print("빠져나간 값 : ",top)
print(stack)

#스택에서 제거하지않고 top값을 가져올때
top = stack[-1]
print(top)
