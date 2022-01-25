def largestMagical(binString):
    # Write your code here

    stack = list(binString)
    print(stack)
    count1 = 0
    count0 = 0

    for i in stack:
        if i == "1":
            count1 += 1
        if i == '0':
            count0 += 1

        



    return

binString = "11011000"
largestMagical(binString)