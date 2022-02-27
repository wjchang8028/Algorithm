# 문자열 리스트에서 특정한 인덱스 값으로 정렬하는 방법

temp = ["abcd","abce","abca","ffca","cde"] # 인덱스2 기준으로 정렬할 것.

print(sorted(temp)) # 맨 앞글자 사전 순 배열
print(sorted(temp, key=lambda x:x[2])) # 인덱스 기준으로만 정렬
print(sorted(sorted(temp),key=lambda x:x[2])) #사전 순으로 정렬 한 뒤, 특정 인덱스 기준으로 정렬

# ['abca', 'abcd', 'abce', 'cde', 'ffca']
# ['abcd', 'abce', 'abca', 'ffca', 'cde']
# ['abca', 'abcd', 'abce', 'ffca', 'cde']