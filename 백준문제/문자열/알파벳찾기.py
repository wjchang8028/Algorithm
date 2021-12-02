word = input()

alphabet = list(range(97,123)) #97~122가 a~z까지의 아스키값

for i in alphabet:
    print(word.find(chr(i))) #chr()는 int를 문자형으로
