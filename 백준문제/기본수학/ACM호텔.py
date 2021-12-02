import sys
case = int(input())

for i in range(case):
    h,w,n = map(int,sys.stdin.readline().split())
    
    if n % h == 0:
        ho = n // h
        floor = h
    else:
        ho = n//h + 1
        floor = n % h

    floor = str(floor)
    ho = str(ho).zfill(2)

    print(floor+ho)

    


