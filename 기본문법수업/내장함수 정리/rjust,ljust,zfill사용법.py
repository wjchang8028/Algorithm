a = '777'

# zfill은 str형태에만 사용가능. zfill(자릿수)
print(a.zfill(5))
# 00777

#rjust는 str형태에서 왼쪽에 자릿수만큼 값 채워주기. rjust(자릿수,'넣을값')
print(a.rjust(5,'#'))
# ##777

print(a.ljust(5,'@'))
# 777@@