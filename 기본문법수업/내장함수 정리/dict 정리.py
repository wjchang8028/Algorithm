                # dictionary 선언
dic1 = {}
dic2 = dict()
print(dic1,dic2) # {} {}



                # dict = {key : value}
dic1["A"] = 1
dic2['옷'] = '니트'
print(dic1,dic2) # {'A': 1} {'옷': '니트'}
print(dic1['A']) # 1
print(dic1.get('B')) # get(키값) 은 키값이 없다면 None 반환


hash_list = {'a':1, 'b':2 , 'c':3}
for key,value in hash_list.items(): # key,value값이 묶인 items()
    print(key,value) 



del dic1['A'] # 키값으로 찾아서 삭제
print(dic1,dic2) # {} {'옷': '니트'}


hash_addlist = [['a',1], ['a',2], ['b',1], ['c',1], ['c',2]]
hash_value = {}
for key,value in hash_addlist:
    hash_value.setdefault(key,[]).append(value) # 각 키값에 빈 배열 선언 후 value를 삽입
print(hash_value) # {'a': [1, 2], 'b': [1], 'c': [1, 2]}
