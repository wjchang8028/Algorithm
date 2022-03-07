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
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력 -> 원래출력은 반대로 나옴
    
print(deciToBin(45, 3))

def convert(n, base): # n진수를 base진법으로 변환하는것 (중요!)
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]

print(convert(15,16))