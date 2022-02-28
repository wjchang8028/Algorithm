num = 40

a = bin(num)
print(a) # 0b101000 2진법 변경

b = int(a,2)
print(b) # 40 2진법을 다시 10진법으로

def deciToBin(num, n): # 10진수에서 n 진수로
    rev_base = ''

    while num > 0:
        num, mod = divmod(num, n)
        rev_base += str(mod)
    print(rev_base)
    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    
print(deciToBin(45, 3))