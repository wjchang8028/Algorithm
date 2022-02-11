# or표현. 전자가 참이면 전자가 출력, 거짓이면 후자가 출력
array = [1,2,3]
print([i for i in array if i % 4 == 0] or [-1] )
# 결과 : [-1]