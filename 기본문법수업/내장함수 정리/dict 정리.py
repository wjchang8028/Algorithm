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


hash_addlist = [['a',1], ['a',2], ['b',1], ['c',1], ['c',2],['c',3]]
hash_value = {}
for key,value in hash_addlist:
    hash_value.setdefault(key,[]).append(value) # 각 키값에 빈 배열 선언 후 value를 삽입
print(hash_value) # {'a': [1, 2], 'b': [1], 'c': [1, 2]}



hash_value2 = {}
for key,value in hash_addlist:
    if key not in hash_value2: # 기본적으로 dic 은 기본값이 있어야 연산이 가능하기 때문에 먼저 선언을 해주고 계산해야함
        hash_value2[key] = 0
    hash_value2[key] += value
print(hash_value2) # {'a': 3, 'b': 1, 'c': 6}

hash_value3 = {}
for key,value in hash_addlist:
    hash_value3.setdefault(key,0) # setdefault는 기본 리스트를 만들어주는것
    hash_value3[key] += value 
print(hash_value3) # {'a': 3, 'b': 1, 'c': 6}