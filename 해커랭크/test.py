def fizzBuzz(n):
    for i in range(1,n+1):

        if i % 3 == 0: #3으로만 나눠질때
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            if i % 3 == 0:
                print("FizzBuzz")
            else:
                print("Buzz")
        
        else:
            print(i)

    return

n = 15
fizzBuzz(n)