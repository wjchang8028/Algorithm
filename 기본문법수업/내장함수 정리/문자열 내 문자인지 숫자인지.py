#문자열 내에 숫자인지 알파벳인지 확인해주는 함수

word = '100ABC'

alphabet_list = []
digit_list = []

print(word.isalpha()) # False
print(word.isdigit()) # False

for i in word:
    if i.isalpha(): # 알파벳들만 모아주기
        alphabet_list.append(i)
    elif i.isdigit(): # 숫자만 모아주기
        digit_list.append(i)

print(digit_list, alphabet_list) # ['1', '0', '0'] ['A', 'B', 'C']