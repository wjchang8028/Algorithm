
def yak(a,b):
    if a > b:
        if a % b == 0:
            return "multiple"
        else:
            return "neither"
    else:
        if b % a == 0:
            return "factor"
        else:
            return "neither"



while True:
    a,b=map(int,input().split())

    if a == b == 0:
        break

    print(yak(a,b))
