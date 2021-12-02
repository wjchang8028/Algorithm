word = input().lower()

word_list = list(set(word)) # word의 중복값 제거

cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count) #카운트한 값을 cnt배열에 저장

if cnt.count(max(cnt)) >=2: #cnt의 max값을 카운트했을때 1초과로 나온다는것은 같은 수가 2개이상 있다는 소리
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())


    